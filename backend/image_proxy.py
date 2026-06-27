import logging

import requests
from flask import Response

from config import Config

logger = logging.getLogger(__name__)


def proxy_image(image_path: str) -> Response:
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
        logger.warning('Image proxy failed: %s', e)
        placeholder = (
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
            b'\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00'
            b'\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00'
            b'\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82'
        )
        return Response(
            placeholder,
            content_type='image/png',
            status=200
        )
