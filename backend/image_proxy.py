import logging
import re

import requests
from flask import Response

from config import Config

logger = logging.getLogger(__name__)

# TMDB 合法图片尺寸段：w45/w92/w154/w185/w300/w342/w500/w780/w1280/h632/original
SIZE_RE = re.compile(r'^/(w\d+|h\d+|original)/')


def _ensure_size(path: str) -> str:
    if SIZE_RE.match(path):
        return path
    return f'/{Config.TMDB_DEFAULT_SIZE}{path}'


def proxy_image(image_path: str) -> Response:
    if not image_path:
        return Response('No image path', status=404, content_type='text/plain')

    final_path = '/' + image_path.lstrip('/')
    final_path = _ensure_size(final_path)
    tmdb_url = f'{Config.TMDB_IMAGE_BASE}{final_path}'

    try:
        resp = requests.get(
            tmdb_url,
            timeout=Config.TMDB_TIMEOUT,
            stream=True
        )
        resp.raise_for_status()
        content_type = resp.headers.get('Content-Type', 'image/jpeg')
        return Response(
            resp.content,
            content_type=content_type,
            status=200
        )
    except requests.RequestException as e:
        logger.warning('Image proxy failed: %s, returning placeholder', e)
        # 返回可见占位 SVG（灰色背景 + 🎬 图标 + 提示文字），而非不可见的 1x1 图
        placeholder = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="450" viewBox="0 0 300 450">'
            '<rect width="300" height="450" fill="#f0f0f0"/>'
            '<text x="150" y="225" font-size="60" text-anchor="middle" fill="#ccc">🎬</text>'
            '<text x="150" y="260" font-size="14" text-anchor="middle" fill="#bbb">图片加载失败</text>'
            '</svg>'
        )
        return Response(
            placeholder,
            content_type='image/svg+xml',
            status=200
        )
