// 视图状态管理（单例）：管理用户的想看/看过/喜欢收藏列表
import { CollectionState, Movie } from '../model/Models';

export class MovieViewModel {
  private static instance: MovieViewModel;
  // 收藏状态：仅保存在内存中，重启后会丢失
  private collectionState: CollectionState = {
    wantToWatch: [],
    watched: [],
    liked: []
  };

  // 获取单例实例
  static getInstance(): MovieViewModel {
    if (!MovieViewModel.instance) {
      MovieViewModel.instance = new MovieViewModel();
    }
    return MovieViewModel.instance;
  }

  // 获取当前收藏状态（包含三个列表）
  getCollection(): CollectionState {
    return this.collectionState;
  }

  // 切换"想看"标记：已存在则移除，不存在则添加
  toggleWantToWatch(movieId: number): void {
    const idx: number = this.collectionState.wantToWatch.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.wantToWatch.splice(idx, 1);
    } else {
      this.collectionState.wantToWatch.push(movieId);
    }
  }

  // 切换"看过"标记
  toggleWatched(movieId: number): void {
    const idx: number = this.collectionState.watched.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.watched.splice(idx, 1);
    } else {
      this.collectionState.watched.push(movieId);
    }
  }

  // 切换"喜欢"标记
  toggleLiked(movieId: number): void {
    const idx: number = this.collectionState.liked.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.liked.splice(idx, 1);
    } else {
      this.collectionState.liked.push(movieId);
    }
  }

  // 查询指定电影是否在"想看"列表中
  isWantToWatch(movieId: number): boolean {
    return this.collectionState.wantToWatch.indexOf(movieId) >= 0;
  }

  // 查询指定电影是否在"看过"列表中
  isWatched(movieId: number): boolean {
    return this.collectionState.watched.indexOf(movieId) >= 0;
  }

  // 查询指定电影是否在"喜欢"列表中
  isLiked(movieId: number): boolean {
    return this.collectionState.liked.indexOf(movieId) >= 0;
  }
}
