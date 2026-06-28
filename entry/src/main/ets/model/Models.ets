// 电影基本数据类型
export interface Movie {
  id: number;
  title: string;
  originalTitle: string;
  // 剧情简介
  overview: string;
  // 海报图片路径（完整 URL）
  posterPath: string;
  // 背景图片路径（完整 URL）
  backdropPath: string;
  releaseDate: string;
  // TMDB 评分（0-10）
  voteAverage: number;
  // TMDB 类型 ID 列表
  genreIds: number[];
  // 类型中文名称列表（由后端翻译）
  genreNames: string[];
}

// 电影详情（继承 Movie，增加演职人员和推荐）
export interface MovieDetail extends Movie {
  // 片长（分钟）
  runtime: number;
  director: string;
  // 演员列表（最多 10 人）
  cast: CastMember[];
  // 相似推荐电影列表
  recommendations: Movie[];
}

// 演员信息
export interface CastMember {
  name: string;
  // 饰演角色名
  character: string;
  // 头像路径
  profilePath: string;
}

// 情绪条目（用于首页情绪推荐功能）
export interface EmotionItem {
  emoji: string;
  label: string;
  // 该情绪映射到的 TMDB 类型 ID 列表
  genreIds: number[];
  // 筛选最低评分
  minRating: number;
  // 推荐文案
  recText: string;
}

// 用户收藏状态
export interface CollectionState {
  wantToWatch: number[];
  watched: number[];
  liked: number[];
}
