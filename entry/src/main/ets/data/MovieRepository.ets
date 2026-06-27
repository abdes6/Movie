import { http } from '@kit.NetworkKit';
import { Constants } from '../common/Constants';
import { Movie, MovieDetail, CastMember } from '../model/Models';

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
    return {
      id: data['id'] as number,
      title: (data['title'] || data['original_title'] || '') as string,
      originalTitle: (data['original_title'] || '') as string,
      overview: (data['overview'] || '') as string,
      posterPath: data['poster_path'] ? `${Constants.IMAGE_BASE_URL}${data['poster_path']}` : '',
      backdropPath: data['backdrop_path'] ? `${Constants.IMAGE_BASE_URL}${data['backdrop_path']}` : '',
      releaseDate: (data['release_date'] || '') as string,
      voteAverage: (data['vote_average'] || 0) as number,
      genreIds: (data['genre_ids'] || []) as number[],
      genreNames: (data['genre_names'] || []) as string[]
    };
  }

  async fetchPopular(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/popular?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchTopRated(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/top_rated?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchNowPlaying(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/now_playing?page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchByGenre(genreIds: number[], page: number = 1): Promise<Movie[]> {
    const ids = genreIds.join(',');
    const url = `${Constants.API_BASE_URL}/discover/movie?with_genres=${ids}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchMovieDetail(movieId: number): Promise<MovieDetail> {
    const url = `${Constants.API_BASE_URL}/movie/${movieId}`;
    const data = await this.fetchJson(url);
    const movie = this.parseMovie(data) as MovieDetail;

    movie.runtime = (data['runtime'] || 0) as number;

    const cast = (data['cast'] || []) as Record<string, Object>[];
    movie.cast = cast.slice(0, 10).map((c: Record<string, Object>): CastMember => ({
      name: (c['name'] || '') as string,
      character: (c['character'] || '') as string,
      profilePath: c['profile_path'] ? `${Constants.IMAGE_BASE_URL}${c['profile_path']}` : ''
    }));

    movie.director = (data['director'] || '') as string;

    const recommendations = (data['recommendations'] || []) as Record<string, Object>[];
    movie.recommendations = recommendations.slice(0, 10).map((item: Record<string, Object>): Movie => this.parseMovie(item));

    const genreNames = (data['genre_names'] || []) as string[];
    movie.genreNames = genreNames;

    return movie;
  }

  async searchMovies(query: string, page: number = 1): Promise<Movie[]> {
    const url = `${Constants.API_BASE_URL}/movie/search?query=${encodeURIComponent(query)}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  async fetchByFilters(genres: number[], minRating: number, page: number = 1): Promise<Movie[]> {
    const genreParam = genres.length > 0 ? `&with_genres=${genres.join(',')}` : '';
    const url = `${Constants.API_BASE_URL}/discover/movie?${genreParam}&vote_average.gte=${minRating}&page=${page}`;
    const data = await this.fetchJson(url);
    const results = (data['results'] || []) as Record<string, Object>[];
    return results.map((item: Record<string, Object>): Movie => this.parseMovie(item));
  }

  destroy(): void {
    this.httpRequest.destroy();
  }
}
