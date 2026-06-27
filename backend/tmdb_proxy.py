import logging
import random
from typing import Any

import requests

from config import Config
from mock_data import (
    MOVIES_POPULAR, MOVIES_TOP_RATED, MOVIES_NOW_PLAYING,
    MOVIE_DETAILS, MOCK_DB, GENRE_MAP
)

logger = logging.getLogger(__name__)

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def _tmdb_url(path: str) -> str:
    return f'{Config.TMDB_BASE_URL}{path}'


def _fetch_or_fallback(
    url: str,
    params: dict | None,
    mock_data: Any,
    parser: callable
) -> Any:
    if not Config.USE_MOCK_FALLBACK:
        try:
            resp = session.get(url, params=params, timeout=Config.TMDB_TIMEOUT)
            resp.raise_for_status()
            return parser(resp.json())
        except requests.RequestException as e:
            logger.warning('TMDB request failed: %s, falling back to mock', e)
            return parser(mock_data)
    return parser(mock_data)


def _parse_movie_list(data: dict) -> dict:
    results = data.get('results', [])
    for movie in results:
        genre_ids = movie.get('genre_ids', [])
        movie['genre_names'] = [GENRE_MAP.get(gid, '') for gid in genre_ids]
    return data


def _pick_random_slice(movies: list, count: int = 20) -> list:
    if len(movies) <= count:
        return movies
    return random.sample(movies, count)


def fetch_popular(page: int = 1) -> dict:
    url = _tmdb_url('/movie/popular')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_POPULAR, _parse_movie_list)


def fetch_top_rated(page: int = 1) -> dict:
    url = _tmdb_url('/movie/top_rated')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_TOP_RATED, _parse_movie_list)


def fetch_now_playing(page: int = 1) -> dict:
    url = _tmdb_url('/movie/now_playing')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_NOW_PLAYING, _parse_movie_list)


def fetch_movie_detail(movie_id: int) -> dict:
    url = _tmdb_url(f'/movie/{movie_id}')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'append_to_response': 'credits,recommendations'
    }

    def parser(data: dict) -> dict:
        credits = data.get('credits', {}) or {}
        crew = credits.get('crew', []) or []
        director = data.get('director', '')
        if not director:
            for c in crew:
                if c.get('job') == 'Director':
                    director = c.get('name', '')
                    break
        data['director'] = director

        cached_cast = data.get('cast', []) or []
        if not cached_cast:
            credits_cast = credits.get('cast', []) or []
            cached_cast = credits_cast
        data['cast'] = [
            {
                'name': a.get('name', ''),
                'character': a.get('character', ''),
                'profile_path': a.get('profile_path', '')
            }
            for a in cached_cast[:10]
        ]

        recs = data.get('recommendations', []) or []
        if isinstance(recs, dict):
            rec_results = recs.get('results', []) or []
        else:
            rec_results = recs
        genre_ids = data.get('genre_ids', []) or []
        data['genre_names'] = [GENRE_MAP.get(gid, '') for gid in genre_ids]
        data['recommendations'] = [
            {
                'id': r.get('id', 0),
                'title': r.get('title', ''),
                'original_title': r.get('original_title', ''),
                'overview': r.get('overview', ''),
                'poster_path': r.get('poster_path', ''),
                'backdrop_path': r.get('backdrop_path', ''),
                'release_date': r.get('release_date', ''),
                'vote_average': r.get('vote_average', 0),
                'genre_ids': r.get('genre_ids', []) or []
            }
            for r in rec_results[:10]
        ]
        return data

    mock_data = MOVIE_DETAILS.get(movie_id)
    if mock_data is None:
        available = list(MOVIE_DETAILS.keys())
        mock_data = MOVIE_DETAILS.get(random.choice(available) if available else 3)

    return _fetch_or_fallback(url, params, mock_data, parser)


def search_movies(query: str, page: int = 1) -> dict:
    url = _tmdb_url('/search/movie')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'query': query,
        'page': page
    }

    def parser(data: dict) -> dict:
        return _parse_movie_list(data)

    def mock_search(_data: dict) -> dict:
        all_movies = list(MOCK_DB['movies'].values())
        q = query.lower()
        matched = [
            m for m in all_movies
            if q in m.get('title', '').lower()
            or q in m.get('original_title', '').lower()
        ]
        return {
            'page': 1,
            'results': _pick_random_slice(matched, 20),
            'total_pages': 1,
            'total_results': len(matched)
        }

    return _fetch_or_fallback(url, params, None, mock_search)


def discover_movies(
    with_genres: str = '',
    vote_average_gte: float = 0,
    page: int = 1
) -> dict:
    url = _tmdb_url('/discover/movie')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'sort_by': 'popularity.desc',
        'vote_count.gte': 50,
        'page': page
    }
    if with_genres:
        params['with_genres'] = with_genres
    if vote_average_gte > 0:
        params['vote_average.gte'] = vote_average_gte

    def parser(data: dict) -> dict:
        return _parse_movie_list(data)

    def mock_discover(_data: dict) -> dict:
        all_movies = list(MOCK_DB['movies'].values())
        filtered = all_movies

        if with_genres:
            genre_ids = [int(g) for g in with_genres.split(',') if g]
            if genre_ids:
                filtered = [
                    m for m in filtered
                    if any(gid in m.get('genre_ids', []) for gid in genre_ids)
                ]

        if vote_average_gte > 0:
            filtered = [
                m for m in filtered
                if m.get('vote_average', 0) >= vote_average_gte
            ]

        return {
            'page': 1,
            'results': _pick_random_slice(filtered, 20),
            'total_pages': 1,
            'total_results': len(filtered)
        }

    return _fetch_or_fallback(url, params, None, mock_discover)
