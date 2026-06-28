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

# 复用 HTTP 连接（连接池），减少三次握手开销
session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def _tmdb_url(path: str) -> str:
    """拼接 TMDB API 完整 URL"""
    return f'{Config.TMDB_BASE_URL}{path}'


def _fetch_or_fallback(
    url: str,
    params: dict | None,
    mock_data: Any,
    parser: callable
) -> Any:
    """
    通用请求模板：优先请求 TMDB，失败或强制 Mock 时降级到本地数据。
    
    - 当 USE_MOCK_FALLBACK=True 时直接返回 Mock 数据
    - 否则先请求 TMDB，网络异常时自动降级到 Mock
    - parser 负责将原始 JSON 转换为需要的数据结构
    """
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
    """解析电影列表，将 genre_ids 翻译为中文类型名"""
    results = data.get('results', [])
    for movie in results:
        genre_ids = movie.get('genre_ids', [])
        movie['genre_names'] = [GENRE_MAP.get(gid, '') for gid in genre_ids]
    return data


def _pick_random_slice(movies: list, count: int = 20) -> list:
    """从列表中随机抽取 count 个元素（不超过列表长度）"""
    if len(movies) <= count:
        return movies
    return random.sample(movies, count)


def fetch_popular(page: int = 1) -> dict:
    """获取 TMDB 热门电影"""
    url = _tmdb_url('/movie/popular')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_POPULAR, _parse_movie_list)


def fetch_top_rated(page: int = 1) -> dict:
    """获取 TMDB 高分电影"""
    url = _tmdb_url('/movie/top_rated')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_TOP_RATED, _parse_movie_list)


def fetch_now_playing(page: int = 1) -> dict:
    """获取 TMDB 正在上映电影"""
    url = _tmdb_url('/movie/now_playing')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'page': page
    }
    return _fetch_or_fallback(url, params, MOVIES_NOW_PLAYING, _parse_movie_list)


def fetch_movie_detail(movie_id: int) -> dict:
    """
    获取电影详情。
    
    使用 TMDB 的 append_to_response 参数一次拉取 credits（演职员表）
    和 recommendations（推荐电影），减少 API 调用次数。
    """
    url = _tmdb_url(f'/movie/{movie_id}')
    params = {
        'api_key': Config.TMDB_API_KEY,
        'language': Config.LANG_ZH,
        'append_to_response': 'credits,recommendations'
    }

    def parser(data: dict) -> dict:
        """解析电影详情，提取导演、演员（取前10）、推荐电影"""
        credits = data.get('credits', {}) or {}
        crew = credits.get('crew', []) or []
        # 从 crew 中找出导演（优先使用缓存，避免重复查找）
        director = data.get('director', '')
        if not director:
            for c in crew:
                if c.get('job') == 'Director':
                    director = c.get('name', '')
                    break
        data['director'] = director

        # 提取前 10 位演员信息
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

        # 处理推荐电影（TMDB 返回结构可能是 dict 或 list）
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

    # 从 MOVIE_DETAILS 中查找，找不到时返回第一个作为兜底
    mock_data = MOVIE_DETAILS.get(movie_id, MOVIE_DETAILS.get(1))

    return _fetch_or_fallback(url, params, mock_data, parser)


def search_movies(query: str, page: int = 1) -> dict:
    """搜索电影（Mock 模式下在本地数据中模糊匹配标题）"""
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
        """Mock 搜索：在 MOCK_DB 中按标题/原名模糊匹配"""
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
    """
    组合条件筛选电影。
    
    支持按类型 ID（逗号分隔）和评分下限过滤。
    Mock 模式下在本地数据中用相同逻辑过滤。
    """
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
        """Mock 筛选：在本地数据中按类型和评分过滤"""
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
