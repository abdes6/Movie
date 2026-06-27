import logging

from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from config import Config
from tmdb_proxy import (
    fetch_popular, fetch_top_rated, fetch_now_playing,
    fetch_movie_detail, search_movies, discover_movies
)
from image_proxy import proxy_image

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


def api_ok(data) -> dict:
    return {'success': True, 'data': data, 'error': None}


def api_error(msg: str, code: int = 400) -> tuple:
    return jsonify({'success': False, 'data': None, 'error': msg}), code


@app.route('/api/movie/popular')
def popular():
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_popular(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch popular failed')
        return api_error(str(e), 500)


@app.route('/api/movie/top_rated')
def top_rated():
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_top_rated(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch top_rated failed')
        return api_error(str(e), 500)


@app.route('/api/movie/now_playing')
def now_playing():
    page = request.args.get('page', 1, type=int)
    try:
        data = fetch_now_playing(page)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch now_playing failed')
        return api_error(str(e), 500)


@app.route('/api/movie/<int:movie_id>')
def detail(movie_id: int):
    try:
        data = fetch_movie_detail(movie_id)
        return jsonify(api_ok(data))
    except Exception as e:
        logger.exception('fetch detail failed')
        return api_error(str(e), 500)


@app.route('/api/movie/search')
def search():
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
    return proxy_image(f'/{image_path}')


@app.route('/api/health')
def health():
    return jsonify(api_ok({'status': 'ok', 'source': 'flask-backend'}))


if __name__ == '__main__':
    logger.info(
        'Starting Flask backend on %s:%s (debug=%s)',
        Config.HOST, Config.PORT, Config.DEBUG
    )
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
