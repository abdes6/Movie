// 🌟 1. 修正：改用鸿蒙官方最新推荐的 NetworkKit 导入
import { http } from '@kit.NetworkKit';
import { Constants } from '../common/Constants';
import { Movie, MovieDetail, CastMember } from '../model/Models';

export class MovieRepository {
  private httpRequest: http.HttpRequest;

  constructor() {
    this.httpRequest = http.createHttp();
  }

  // 🌟 2. 修正：将显式 any 规避为通用对象结构，并严格加上 Promise 返回值声明
  private async fetchJson(url: string): Promise<Record<string, Object>> {
    return new Promise<Record<string, Object>>((resolve: (value: Record<string, Object>) => void, reject: (reason: Error) => void): void => {
      this.httpRequest.request(url, {
        method: http.RequestMethod.GET,
        header: { 'Content-Type': 'application/json' },
        connectTimeout: 10000,
        readTimeout: 10000
      }, (err: Error, resp: http.HttpResponse): void => { // 🌟 显式指定回调函数返回 void
        if (err) {
          reject(err);
          return;
        }
        resolve(JSON.parse(resp.result as string) as Record<string, Object>);
      });
    });
  }

  // 🌟 3. 修正：规避入参 data: any，显式指定返回值为 Movie 实体
  private parseMovie(data: Record<string, Object>): Movie {
    return {
      id: data['id'] as number,
      title: (data['title'] || data['original_title'] || '') as string,
      originalTitle: (data['original_title'] || '') as string,
      overview: (data['overview'] || '') as string,
      posterPath: data['poster_path'] ? `${Constants.TMDB_IMAGE_BASE}${data['poster_path']}` : '',
      backdropPath: data['backdrop_path'] ? `${Constants.TMDB_IMAGE_BASE}${data['backdrop_path']}` : '',
      releaseDate: (data['release_date'] || '') as string,
      voteAverage: (data['vote_average'] || 0) as number,
      genreIds: (data['genre_ids'] || []) as number[],
      genreNames: []
    };
  }

  async fetchPopular(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/popular?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    // 🌟 4. 修正：极其严苛的匿名箭头函数必须要声明类型 (item): Movie => { ... }
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchTopRated(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/top_rated?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchNowPlaying(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/now_playing?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchByGenre(genreIds: number[], page: number = 1): Promise<Movie[]> {
    const ids = genreIds.join(',');
    const url = `${Constants.TMDB_BASE_URL}/discover/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&with_genres=${ids}&sort_by=vote_average.desc&vote_count.gte=100&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchMovieDetail(movieId: number): Promise<MovieDetail> {
    const url = `${Constants.TMDB_BASE_URL}/movie/${movieId}?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&append_to_response=credits,recommendations`;
    const data = await this.fetchJson(url);
    const movie = this.parseMovie(data) as MovieDetail;

    movie.runtime = (data['runtime'] || 0) as number;

    const credits = data['credits'] as Record<string, Object> || {};
    const crew = (credits['crew'] || []) as Record<string, Object>[];
    // 🌟 修正：.find((c): boolean => ...) 显式强制指明返回布尔类型断言
    const directorObj = crew.find((c: Record<string, Object>): boolean => c['job'] === 'Director');
    movie.director = directorObj ? (directorObj['name'] as string) : '';

    const cast = (credits['cast'] || []) as Record<string, Object>[];
    movie.cast = cast.slice(0, 10).map((c: Record<string, Object>): CastMember => ({
      name: (c['name'] || '') as string,
      character: (c['character'] || '') as string,
      profilePath: c['profile_path'] ? `${Constants.TMDB_IMAGE_BASE}${c['profile_path']}` : ''
    }));

    const recommendations = data['recommendations'] as Record<string, Object> || {};
    const recResults = (recommendations['results'] || []) as Record<string, Object>[];
    movie.recommendations = recResults.slice(0, 10).map((item: Record<string, Object>): Movie => this.parseMovie(item));

    const genres = (data['genres'] || []) as Record<string, Object>[];
    movie.genreNames = genres.map((g: Record<string, Object>): string => (g['name'] || '') as string);

    return movie;
  }

  async searchMovies(query: string, page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/search/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&query=${encodeURIComponent(query)}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchByFilters(genres: number[], minRating: number, page: number = 1): Promise<Movie[]> {
    const genreParam = genres.length > 0 ? `&with_genres=${genres.join(',')}` : '';
    const url = `${Constants.TMDB_BASE_URL}/discover/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}${genreParam}&vote_average.gte=${minRating}&vote_count.gte=50&sort_by=popularity.desc&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  destroy(): void { // 🌟 显式补全普通函数的返回类型
    this.httpRequest.destroy();
  }
}