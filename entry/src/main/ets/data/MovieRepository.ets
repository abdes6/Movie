import { http } from '@kit.NetworkKit';
import { Constants } from '../common/Constants';
import { Movie, MovieDetail, CastMember } from '../model/Models';

const SIZE_RE: RegExp = /^\/(w\d+|h\d+|original)\//;

function buildImageUrl(path: string | undefined, defaultSize: string = '/w500'): string {
  if (!path) return Constants.FALLBACK_POSTER;
  if (path.startsWith('http')) return path;
  const sized = SIZE_RE.test(path) ? path : `${defaultSize}${path}`;
  return `${Constants.TMDB_CDN_BASE}${sized}`;
}

export class MovieRepository {
  private httpRequest: http.HttpRequest;

  constructor() {
    this.httpRequest = http.createHttp();
  }

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

  private parseMovie(data: Record<string, Object>): Movie {
    const posterPath: string = buildImageUrl(data['poster_path'] as string | undefined);
    const backdropPath: string = buildImageUrl(data['backdrop_path'] as string | undefined);
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

    const cast = (data['cast'] || []) as Record<string, Object>[];
    movie.cast = cast.slice(0, 10).map((c: Record<string, Object>): CastMember => {
      return {
        name: (c['name'] || '') as string,
        character: (c['character'] || '') as string,
        profilePath: buildImageUrl(c['profile_path'] as string | undefined, '/w185')
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
