import os


class Config:
    HOST: str = os.getenv('FLASK_HOST', '0.0.0.0')
    PORT: int = int(os.getenv('FLASK_PORT', '5000'))
    DEBUG: bool = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'

    TMDB_BASE_URL: str = 'https://api.themoviedb.org/3'
    TMDB_API_KEY: str = os.getenv(
        'TMDB_API_KEY',
        'edb8215195923ea4410a96771ef5899d'
    )
    TMDB_IMAGE_BASE: str = 'https://image.tmdb.org/t/p/w500'
    LANG_ZH: str = 'zh-CN'

    TMDB_TIMEOUT: int = 10

    USE_MOCK_FALLBACK: bool = os.getenv(
        'USE_MOCK_FALLBACK', 'true'
    ).lower() == 'true'
