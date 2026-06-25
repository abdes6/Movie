export class Constants {
  static readonly TMDB_BASE_URL = 'https://api.themoviedb.org/3';
  static readonly TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p/w500';
  static readonly TMDB_API_KEY = 'edb8215195923ea4410a96771ef5899d';
  static readonly LANG_ZH = 'zh-CN';

  static readonly GENRES: Record<string, number> = {
    '动作': 28, '冒险': 12, '动画': 16, '喜剧': 35, '犯罪': 80,
    '纪录片': 99, '剧情': 18, '家庭': 10751, '奇幻': 14, '历史': 36,
    '恐怖': 27, '音乐': 10402, '悬疑': 9648, '爱情': 10749,
    '科幻': 878, '惊悚': 53, '战争': 10752, '西部': 37
  };

  static readonly GENRE_KEYS: string[] = Object.keys(Constants.GENRES);
}
