// 数据仓库层：封装所有后端 API 调用，将响应数据解析为前端 Model
import { http } from '@kit.NetworkKit';
import { Constants } from '../common/Constants';
import { Movie, MovieDetail, CastMember } from '../model/Models';

export class MovieRepository {
  private httpRequest: http.HttpRequest;

  constructor() {
    this.httpRequest = http.createHttp();
  }

  // 通用 GET 请求，返回解析后的 JSON 对象
  private async fetchJson(url: string): Promise<Record<string, Object>> {
    return new Promise<Record<string, Object>>((resolve: (value: Record<string, Object>) => void, reject: (reason: Error) => void): void => {
      this.httpRequest.request(url, {
        method: http.RequestMethod.GET,
        header: { 'Content-Type': 'application/json' },
        connectTimeout: 10000,
        readTimeout: 10000
      }, (err: Error, resp: http.HttpResponse): void => {
        if (err) {
          reject(err);
          return;
        }
        resolve(JSON.parse(resp.result as string) as Record<string, Object>);
      });
    });
  }

  // 将后端返回的原始电影数据解析为 Movie 对象
  private parseMovie(data: Record<string, Object>): Movie {
    // 图片 URL 拼接逻辑（三档优先级）：
    // 1. poster_path 以 http 开头 → 直接作为绝对路径使用（如豆瓣图床）
    // 2. poster_path 有值 → 拼接 TMDB CDN 前缀
    // 3. poster_path 为 null/空 → 使用兜底占位图
    const rawPoster = data['poster_path'] as string | undefined;
    const rawBackdrop = data['backdrop_path'] as string | undefined;
    const posterPath: string = rawPoster
      ? rawPoster.startsWith('http')
        ? rawPoster
        : `${Constants.TMDB_CDN_BASE}${rawPoster}`
      : Constants.FALLBACK_POSTER;
    const backdropPath: string = rawBackdrop
      ? rawBackdrop.startsWith('http')
        ? rawBackdrop
        : `${Constants.TMDB_CDN_BASE}${rawBackdrop}`
      : Constants.FALLBACK_POSTER;
    return {
      id: data['id'] as number,
      title: (data['title'] || data['original_title'] || '') as string,
      originalTitle: (data['original_title'] || '') as string,
      overview: (data['overview'] || '') as string,
      posterPath: posterPath,
      backdropPath: backdropPath,
      releaseDate: (data['release_date'] || '') as string,
      voteAverage: (data['vote_average'] || 0) as number,
      genreIds: (data['genre_ids'] || []) as number[],
      genreNames: (data['genre_names'] || []) as string[]
    };
  }

  // 获取热门电影列表
  async fetchPopular(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/popular?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 获取高分电影列表
  async fetchTopRated(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/top_rated?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 获取正在上映电影列表
  async fetchNowPlaying(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/now_playing?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 根据类型 ID 列表筛选电影
  async fetchByGenre(genreIds: number[], page: number = 1): Promise<Movie[]> {
    const ids = genreIds.join(',');
    const url = `${Constants.API_BASE_URL}/discover/movie?with_genres=${ids}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 获取电影详情（含演员、推荐）
  async fetchMovieDetail(movieId: number): Promise<MovieDetail> {
    const url = `${Constants.API_BASE_URL}/movie/${movieId}`;
    const data = await this.fetchJson(url);
    const movie = this.parseMovie(data) as MovieDetail;

    movie.runtime = (data['runtime'] || 0) as number;

    // 解析演员列表（取前 10 人）
    const cast = (data['cast'] || []) as Record<string, Object>[];
    movie.cast = cast.slice(0, 10).map((c: Record<string, Object>): CastMember => {
      const rawProfile = c['profile_path'] as string | undefined;
      return {
        name: (c['name'] || '') as string,
        character: (c['character'] || '') as string,
        profilePath: rawProfile
          ? rawProfile.startsWith('http')
            ? rawProfile
            : `${Constants.TMDB_CDN_BASE}${rawProfile}`
          : Constants.FALLBACK_POSTER
      };
    });

    movie.director = (data['director'] || '') as string;

    // 解析推荐电影（取前 10 部）
    const recommendations = (data['recommendations'] || []) as Record<string, Object>[];
    movie.recommendations = recommendations.slice(0, 10).map((item: Record<string, Object>): Movie => this.parseMovie(item));

    const genreNames = (data['genre_names'] || []) as string[];
    movie.genreNames = genreNames;

    return movie;
  }

  // 搜索电影（模糊匹配标题）
  async searchMovies(query: string, page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/search?query=${encodeURIComponent(query)}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 组合筛选：按类型 + 评分下限
  async fetchByFilters(genres: number[], minRating: number, page: number = 1): Promise<Movie[]> {
    const genreParam = genres.length > 0 ? `&with_genres=${genres.join(',')}` : '';
    const url = `${Constants.API_BASE_URL}/discover/movie?${genreParam}&vote_average.gte=${minRating}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  // 释放 HTTP 连接资源
  destroy(): void {
    this.httpRequest.destroy();
  }
}
