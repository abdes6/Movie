import logging

import requests
from flask import Response

from config import Config

logger = logging.getLogger(__name__)


def proxy_image(image_path: str) -> Response:
    """
    代理 TMDB 图片请求。
    
    前端通过此接口间接加载 TMDB 图片，避免直接暴露第三方 CDN 地址。
    请求失败时返回一个 1x1 像素的透明 PNG 占位图（而非报错），
    避免前端 Image 组件显示红叉。
    """
    if not image_path:
        return Response('No image path', status=404, content_type='text/plain')

    tmdb_url = f'{Config.TMDB_IMAGE_BASE}{image_path}'

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
