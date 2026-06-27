import { CollectionState, Movie } from '../model/Models';

export class MovieViewModel {
  private static instance: MovieViewModel;
  private collectionState: CollectionState = {
    wantToWatch: [],
    watched: [],
    liked: []
  };

  static getInstance(): MovieViewModel {
    if (!MovieViewModel.instance) {
      MovieViewModel.instance = new MovieViewModel();
    }
    return MovieViewModel.instance;
  }

  getCollection(): CollectionState {
    return this.collectionState;
  }

  toggleWantToWatch(movieId: number): void {
    const idx: number = this.collectionState.wantToWatch.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.wantToWatch.splice(idx, 1);
    } else {
      this.collectionState.wantToWatch.push(movieId);
    }
  }

  toggleWatched(movieId: number): void {
    const idx: number = this.collectionState.watched.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.watched.splice(idx, 1);
    } else {
      this.collectionState.watched.push(movieId);
    }
  }

  toggleLiked(movieId: number): void {
    const idx: number = this.collectionState.liked.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.liked.splice(idx, 1);
    } else {
      this.collectionState.liked.push(movieId);
    }
  }

  isWantToWatch(movieId: number): boolean {
    return this.collectionState.wantToWatch.indexOf(movieId) >= 0;
  }

  isWatched(movieId: number): boolean {
    return this.collectionState.watched.indexOf(movieId) >= 0;
  }

  isLiked(movieId: number): boolean {
    return this.collectionState.liked.indexOf(movieId) >= 0;
  }
}
