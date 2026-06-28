import logging

from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from config import Config
from tmdb_proxy import (
    fetch_popular, fetch_top_rated, fetch_now_playing,
    fetch_movie_detail, search_movies, discover_movies
)
from image_proxy import proxy_image

# 配置日志格式：时间 [级别] 模块名: 消息
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

# 创建 Flask 应用，允许跨域请求（前端开发时跨端口调用）
app = Flask(__name__)
CORS(app)

import requests

def api_ok(data) -> dict:
    """构造统一成功响应体"""
    return {'success': True, 'data': data, 'error': None}


def api_error(msg: str, code: int = 400) -> tuple:
    """构造统一错误响应体，返回 (JSON, HTTP状态码)"""
    return jsonify({'success': False, 'data': None, 'error': msg}), code

import requests


@app.route('/')
def get_tmdb_data():
    # 🌟 1. 定义常量（如果国内反代可用，把 BASE_URL 换成反代域名）
    BASE_URL = "https://api.themoviedb.org/3"
    API_KEY = 'edb8215195923ea4410a96771ef5899d'

    # 🌟 2. 拼接你想获取的功能路由（例如：获取高分经典电影）
    target_url = f"{BASE_URL}/movie/top_rated"

    # 🌟 3. 组装请求参数（指定中文语言，避免满屏英文）
    query_params = {
        "api_key": API_KEY,
        "language": "zh-CN",
        "page": 1
    }

    try:
        # 🌟 4. 发起网络请求
        response = requests.get(target_url, params=query_params, timeout=10)

        # 🌟 5. 如果响应状态码是 200 (OK)
        if response.status_code == 200:
            data = response.json()

            # TMDB 的列表数据全部放在 'results' 这个数组里
            movie_list = data.get("results", [])
            print(f"成功捕获到 {len(movie_list)} 部高分电影！")
            return movie_list
        else:
            print(f"请求失败，TMDB服务器拒绝，状态码: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"网络彻底断流或超时: {e}")
        return []

@app.route('/api/movie/popular')
def popular():
    """获取热门电影列表"""
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_popular(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch popular failed')
        return api_error(str(e), 500)


@app.route('/api/movie/top_rated')
def top_rated():
    """无法获取高分电影列表"""
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_top_rated(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch top_rated failed')
        return api_error(str(e), 500)


@app.route('/api/movie/now_playing')
def now_playing():
    """获取正在上映电影列表"""
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_now_playing(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch now_playing failed')
        return api_error(str(e), 500)


@app.route('/api/movie/<int:movie_id>')
def detail(movie_id: int):
    """获取单个电影的详细信息（含演员、推荐）"""
    try:
        data = fetch_movie_detail(movie_id)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch detail failed')
        return api_error(str(e), 500)


@app.route('/api/movie/search')
def search():
    """搜索电影（模糊匹配标题）"""
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)
    if not query.strip():
        return api_error('query is required')
    try:
        data = search_movies(query, page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('search failed')
        return api_error(str(e), 500)


@app.route('/api/discover/movie')
def discover():
    """组合条件筛选电影（按类型 + 评分下限）"""
    with_genres = request.args.get('with_genres', '', type=str)
    vote_average_gte = request.args.get('vote_average.gte', 0, type=float)
    page = request.args.get('page', 1, type=int)
    try:
        data = discover_movies(with_genres, vote_average_gte, page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('discover failed')
        return api_error(str(e), 500)


@app.route('/api/image/<path:image_path>')
def image(image_path: str) -> Response:
    """代理 TMDB 图片请求，避免前端直连 TMCD CDN"""
    return proxy_image(f'/{image_path}')


@app.route('/api/health')
def health():
    """健康检查端点"""
    return jsonify(api_ok({'status': 'ok', 'source': 'flask-backend'}))


if __name__ == '__main__':
    logger.info(
        'Starting Flask backend on %s:%s (debug=%s)',
        Config.HOST, Config.PORT, Config.DEBUG
    )
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
