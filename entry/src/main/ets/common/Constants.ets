// 应用全局常量配置
export class Constants {
  // Flask 后端 API 地址（开发环境指向本地）
  static readonly API_BASE_URL: string = 'http://127.0.0.1:5000/api';
  // TMDB 图片 CDN 根地址（不含尺寸，由 buildImageUrl 在路径中补充）
  static readonly TMDB_CDN_BASE: string = 'https://image.tmdb.org/t/p';
  // poster_path 为 null/空时的兜底海报（内联 SVG 占位图）
  static readonly FALLBACK_POSTER: string = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300"><rect fill="%23f0f0f0" width="200" height="300"/><text x="100" y="155" text-anchor="middle" font-size="60" fill="%23ccc">🎬</text></svg>';
  // TMDB API 密钥（仅用作本地兜底，后端已配置）
  static readonly TMDB_API_KEY = 'edb8215195923ea4410a96771ef5899d';
  static readonly LANG_ZH = 'zh-CN';

  // TMDB 类型中文名 → 类型 ID 映射表
  static readonly GENRES: Record<string, number> = {
    '动作': 28, '冒险': 12, '动画': 16, '喜剧': 35, '犯罪': 80,
    '纪录片': 99, '剧情': 18, '家庭': 10751, '奇幻': 14, '历史': 36,
    '恐怖': 27, '音乐': 10402, '悬疑': 9648, '爱情': 10749,
    '科幻': 878, '惊悚': 53, '战争': 10752, '西部': 37
  };

  // 类型中文名列表（用于 UI 渲染）
  static readonly GENRE_KEYS: string[] = Object.keys(Constants.GENRES);
}
