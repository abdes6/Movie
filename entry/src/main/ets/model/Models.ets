export interface Movie {
  id: number;
  title: string;
  originalTitle: string;
  overview: string;
  posterPath: string;
  backdropPath: string;
  releaseDate: string;
  voteAverage: number;
  genreIds: number[];
  genreNames: string[];
}

export interface MovieDetail extends Movie {
  runtime: number;
  director: string;
  cast: CastMember[];
  recommendations: Movie[];
}

export interface CastMember {
  name: string;
  character: string;
  profilePath: string;
}

export interface EmotionItem {
  emoji: string;
  label: string;
  genreIds: number[];
  minRating: number;
  recText: string;
}

export interface CollectionState {
  wantToWatch: number[];
  watched: number[];
  liked: number[];
}
