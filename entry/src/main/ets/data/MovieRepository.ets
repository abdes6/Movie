import http from '@ohos.net.http';
import { Constants } from '../common/Constants';
import { Movie, MovieDetail, CastMember } from '../model/Models';

export class MovieRepository {
  private httpRequest: http.HttpRequest;

  constructor() {
    this.httpRequest = http.createHttp();
  }

  private async fetchJson(url: string): Promise<any> {
    return new Promise((resolve, reject) => {
      this.httpRequest.request(url, {
        method: http.RequestMethod.GET,
        header: { 'Content-Type': 'application/json' },
        connectTimeout: 10000,
        readTimeout: 10000
      }, (err, resp) => {
        if (err) {
          reject(err);
          return;
        }
        resolve(JSON.parse(resp.result as string));
      });
    });
  }

  private parseMovie(data: any): Movie {
    return {
      id: data.id,
      title: data.title || data.original_title,
      originalTitle: data.original_title,
      overview: data.overview || '',
      posterPath: data.poster_path ? `${Constants.TMDB_IMAGE_BASE}${data.poster_path}` : '',
      backdropPath: data.backdrop_path ? `${Constants.TMDB_IMAGE_BASE}${data.backdrop_path}` : '',
      releaseDate: data.release_date || '',
      voteAverage: data.vote_average || 0,
      genreIds: data.genre_ids || [],
      genreNames: []
    };
  }

  async fetchPopular(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/popular?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  async fetchTopRated(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/top_rated?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  async fetchNowPlaying(page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/movie/now_playing?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  async fetchByGenre(genreIds: number[], page: number = 1): Promise<Movie[]> {
    const ids = genreIds.join(',');
    const url = `${Constants.TMDB_BASE_URL}/discover/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&with_genres=${ids}&sort_by=vote_average.desc&vote_count.gte=100&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  async fetchMovieDetail(movieId: number): Promise<MovieDetail> {
    const url = `${Constants.TMDB_BASE_URL}/movie/${movieId}?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&append_to_response=credits,recommendations`;
    const data = await this.fetchJson(url);
    const movie = this.parseMovie(data) as MovieDetail;
    movie.runtime = data.runtime || 0;
    movie.director = (data.credits?.crew || [])
      .find((c: any) => c.job === 'Director')?.name || '';
    movie.cast = (data.credits?.cast || []).slice(0, 10).map((c: any) => ({
      name: c.name,
      character: c.character,
      profilePath: c.profile_path ? `${Constants.TMDB_IMAGE_BASE}${c.profile_path}` : ''
    }));
    movie.recommendations = (data.recommendations?.results || []).slice(0, 10).map((item: any) => this.parseMovie(item));
    movie.genreNames = (data.genres || []).map((g: any) => g.name);
    return movie;
  }

  async searchMovies(query: string, page: number = 1): Promise<Movie[]> {
    const url = `${Constants.TMDB_BASE_URL}/search/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}&query=${encodeURIComponent(query)}&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  async fetchByFilters(genres: number[], minRating: number, page: number = 1): Promise<Movie[]> {
    const genreParam = genres.length > 0 ? `&with_genres=${genres.join(',')}` : '';
    const url = `${Constants.TMDB_BASE_URL}/discover/movie?api_key=${Constants.TMDB_API_KEY}&language=${Constants.LANG_ZH}${genreParam}&vote_average.gte=${minRating}&vote_count.gte=50&sort_by=popularity.desc&page=${page}`;
    const data = await this.fetchJson(url);
    return (data.results || []).map((item: any) => this.parseMovie(item));
  }

  destroy() {
    this.httpRequest.destroy();
  }
}
