import pytest


class TestHealth:
    def test_health_returns_ok(self, client):
        resp = client.get('/api/health')
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['success'] is True
        assert data['data']['status'] == 'ok'
        assert data['error'] is None


class TestMovieList:
    LIST_ENDPOINTS = [
        ('/api/movie/popular', 'popular'),
        ('/api/movie/top_rated', 'top_rated'),
        ('/api/movie/now_playing', 'now_playing'),
    ]

    @pytest.mark.parametrize('endpoint,name', LIST_ENDPOINTS)
    def test_list_returns_movies(self, client, endpoint, name):
        resp = client.get(endpoint)
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['success'] is True
        assert data['error'] is None
        assert 'results' in data['data']
        for movie in data['data']['results']:
            self._assert_movie_fields(movie)

    def test_list_supports_pagination(self, client):
        for endpoint, _ in self.LIST_ENDPOINTS:
            resp = client.get(f'{endpoint}?page=1')
            assert resp.status_code == 200

    def test_popular_has_reasonable_count(self, client):
        resp = client.get('/api/movie/popular')
        data = resp.get_json()
        assert len(data['data']['results']) >= 1

    def test_top_rated_high_scores(self, client):
        resp = client.get('/api/movie/top_rated')
        data = resp.get_json()
        for movie in data['data']['results']:
            assert movie['vote_average'] >= 7.0, \
                f"电影 '{movie['title']}' 评分 {movie['vote_average']} 过低"

    def _assert_movie_fields(self, movie):
        assert 'id' in movie and isinstance(movie['id'], int)
        assert 'title' in movie and isinstance(movie['title'], str)
        assert 'poster_path' in movie
        assert 'vote_average' in movie
        assert 'genre_ids' in movie
        assert 'genre_names' in movie
        if movie['genre_names']:
            for name in movie['genre_names']:
                assert isinstance(name, str) and len(name) > 0


class TestMovieDetail:
    def test_detail_contains_all_fields(self, client):
        resp = client.get('/api/movie/1')
        data = resp.get_json()
        assert resp.status_code == 200
        detail = data['data']
        assert detail['id'] == 1
        assert detail['title'] == '流浪地球3'
        assert 'director' in detail and isinstance(detail['director'], str)
        assert 'runtime' in detail and isinstance(detail['runtime'], int)
        assert 'cast' in detail and isinstance(detail['cast'], list)
        assert 'recommendations' in detail and isinstance(detail['recommendations'], list)
        assert 'genre_names' in detail and isinstance(detail['genre_names'], list)

    def test_detail_has_director(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        assert detail['director'] == '郭帆'

    def test_detail_has_cast(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        assert len(detail['cast']) > 0
        for actor in detail['cast']:
            assert 'name' in actor
            assert 'character' in actor
            assert 'profile_path' in actor

    def test_detail_cast_limited_to_10(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        assert len(detail['cast']) <= 10

    def test_detail_recommendations_limited_to_10(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        assert len(detail['recommendations']) <= 10

    def test_detail_recommendations_have_fields(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        for rec in detail['recommendations']:
            assert 'id' in rec
            assert 'title' in rec
            assert 'poster_path' in rec
            assert 'vote_average' in rec

    def test_detail_unknown_id_falls_back(self, client):
        resp = client.get('/api/movie/9999')
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['success'] is True
        assert 'title' in data['data']
        assert 'director' in data['data']


class TestSearch:
    def test_search_returns_results(self, client):
        resp = client.get('/api/movie/search?query=流浪')
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['success'] is True
        assert len(data['data']['results']) > 0
        titles = [m['title'] for m in data['data']['results']]
        assert any('流浪' in t for t in titles), f"搜索结果未包含'流浪'，实际结果: {titles}"

    def test_search_matches_original_title(self, client):
        resp = client.get('/api/movie/search?query=Interstellar')
        data = resp.get_json()
        assert data['success'] is True
        titles = [m['title'] for m in data['data']['results']]
        assert '星际穿越' in titles

    def test_search_empty_query_returns_400(self, client):
        resp = client.get('/api/movie/search')
        data = resp.get_json()
        assert resp.status_code == 400
        assert data['success'] is False
        assert data['error'] == 'query is required'

    def test_search_no_match_returns_empty(self, client):
        resp = client.get('/api/movie/search?query=__不存在的电影__')
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['success'] is True
        assert len(data['data']['results']) == 0


class TestDiscover:
    def test_discover_all_returns_results(self, client):
        resp = client.get('/api/discover/movie')
        data = resp.get_json()
        assert resp.status_code == 200
        assert len(data['data']['results']) > 0

    def test_discover_by_genre(self, client):
        resp = client.get('/api/discover/movie?with_genres=28')
        data = resp.get_json()
        assert data['success'] is True
        for movie in data['data']['results']:
            assert 28 in movie['genre_ids'], \
                f"电影 '{movie['title']}' 不包含动作类型"

    def test_discover_by_rating(self, client):
        resp = client.get('/api/discover/movie?vote_average.gte=9.0')
        data = resp.get_json()
        assert data['success'] is True
        for movie in data['data']['results']:
            assert movie['vote_average'] >= 9.0, \
                f"电影 '{movie['title']}' 评分 {movie['vote_average']} < 9.0"

    def test_discover_by_genre_and_rating(self, client):
        resp = client.get('/api/discover/movie?with_genres=878&vote_average.gte=8.0')
        data = resp.get_json()
        assert data['success'] is True
        for movie in data['data']['results']:
            assert 878 in movie['genre_ids']
            assert movie['vote_average'] >= 8.0


class TestResponseFormat:
    def test_success_response_structure(self, client):
        resp = client.get('/api/movie/popular')
        data = resp.get_json()
        assert set(data.keys()) == {'success', 'data', 'error'}

    def test_error_response_structure(self, client):
        resp = client.get('/api/movie/search')
        data = resp.get_json()
        assert set(data.keys()) == {'success', 'data', 'error'}

    def test_error_response_has_message(self, client):
        resp = client.get('/api/movie/search')
        data = resp.get_json()
        assert data['error'] is not None
        assert len(data['error']) > 0


class TestImageInfoInMovie:
    def test_poster_path_present(self, client, popular_data):
        for movie in popular_data['data']['results']:
            assert movie['poster_path'] is not None
            assert isinstance(movie['poster_path'], str)

    def test_poster_path_not_empty(self, client, popular_data):
        for movie in popular_data['data']['results']:
            assert movie['poster_path'] != '', f"电影 '{movie['title']}' 缺少海报"

    def test_backdrop_path_present_in_detail(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        assert 'backdrop_path' in detail
        assert detail['backdrop_path'] != ''

    def test_cast_profile_path_present(self, client):
        resp = client.get('/api/movie/1')
        detail = resp.get_json()['data']
        for actor in detail['cast']:
            assert 'profile_path' in actor
