import os


class Config:
    # Flask 服务绑定地址，默认监听所有网络接口
    HOST: str = os.getenv('FLASK_HOST', '0.0.0.0')
    # Flask 服务端口
    PORT: int = int(os.getenv('FLASK_PORT', '5000'))
    # 是否开启调试模式（默认开启）
    DEBUG: bool = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'

    # TMDB API 基础地址
    TMDB_BASE_URL: str = 'https://api.themoviedb.org/3'
    # TMDB API 密钥，可通过环境变量覆盖（代码内保留了开发用密钥作为兜底）
    TMDB_API_KEY: str = os.getenv(
        'TMDB_API_KEY',
        'edb8215195923ea4410a96771ef5899d'
    )
    # TMDB 图片 CDN 根地址（不含尺寸，尺寸由 TMDB_DEFAULT_SIZE 或路径指定）
    TMDB_IMAGE_BASE: str = 'https://image.tmdb.org/t/p'
    # 默认图片尺寸（当前端/代理未指定尺寸时使用）
    TMDB_DEFAULT_SIZE: str = 'w500'
    # TMDB API 请求语言（中文）
    LANG_ZH: str = 'zh-CN'

    # TMDB HTTP 请求超时时间（秒）
    TMDB_TIMEOUT: int = 10

    # 是否强制使用 Mock 数据（关闭后会先请求 TMDB，失败后自动降级到 Mock）
    USE_MOCK_FALLBACK: bool = os.getenv(
        'USE_MOCK_FALLBACK', 'true'
    ).lower() == 'true'
