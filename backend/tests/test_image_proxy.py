import pytest
from unittest import mock
import requests

from config import Config


class TestImageProxy:
    VALID_IMAGE_PATH = '/mock/poster_wandering_earth.jpg'

    def test_proxy_returns_image_for_valid_path(self, client):
        resp = client.get(f'/api/image{self.VALID_IMAGE_PATH}')
        assert resp.status_code == 200
        assert resp.content_type.startswith('image/')
        assert len(resp.data) > 0

    def test_proxy_fallback_is_svg(self, client):
        resp = client.get(f'/api/image{self.VALID_IMAGE_PATH}')
        assert b'<svg' in resp.data, "降级图片不是 SVG 格式"

    def test_proxy_empty_path_returns_404(self, client):
        resp = client.get('/api/image/')
        assert resp.status_code == 404

    def test_proxy_fallback_has_correct_content_type(self, client):
        resp = client.get(f'/api/image{self.VALID_IMAGE_PATH}')
        assert resp.content_type == 'image/svg+xml'

    def test_multiple_image_requests(self, client):
        paths = [
            '/mock/poster_wandering_earth.jpg',
            '/mock/poster_nezha.jpg',
            '/mock/poster_shawshank.jpg',
        ]
        for path in paths:
            resp = client.get(f'/api/image{path}')
            assert resp.status_code == 200
            assert b'<svg' in resp.data


class TestImageProxyWithMock:
    @mock.patch('image_proxy.requests.get')
    def test_proxy_passthrough_on_success(self, mock_get, client):
        fake_image_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01'
        mock_resp = mock.MagicMock()
        mock_resp.content = fake_image_data
        mock_resp.headers = {'Content-Type': 'image/jpeg'}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        resp = client.get('/api/image/w500/poster.jpg')

        assert resp.status_code == 200
        assert resp.data == fake_image_data
        assert resp.content_type == 'image/jpeg'

    @mock.patch('image_proxy.requests.get')
    def test_proxy_calls_tmdb_with_correct_url(self, mock_get, client):
        mock_resp = mock.MagicMock()
        mock_resp.content = b'fake'
        mock_resp.headers = {'Content-Type': 'image/jpeg'}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        client.get('/api/image/w500/poster.jpg')

        expected_url = f'{Config.TMDB_IMAGE_BASE}/w500/poster.jpg'
        mock_get.assert_called_once_with(
            expected_url,
            timeout=Config.TMDB_TIMEOUT,
            stream=True
        )

    @mock.patch('image_proxy.requests.get')
    def test_proxy_fallback_on_network_error(self, mock_get, client):
        mock_get.side_effect = requests.RequestException('Connection failed')

        resp = client.get('/api/image/w500/poster.jpg')

        assert resp.status_code == 200
        assert resp.content_type == 'image/svg+xml'
        assert b'<svg' in resp.data
