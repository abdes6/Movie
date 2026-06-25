# 电影发现引擎 App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Build a HarmonyOS movie discovery app with emotion-based recommendation and tag filtering, powered by TMDB API.

**Architecture:** Single-page tab-based navigation with separate detail page. TMDB data fetched via http module. Emotion-to-genre mapping handled client-side. Collection state persisted via AppStorage.

**Tech Stack:** HarmonyOS ArkTS, ArkUI (Tabs, Swiper, Grid), TMDB API, http module

## Global Constraints

- Use `@ohos.net.http` for API calls
- No third-party dependencies — use only HarmonyOS built-in kits
- All UI in ArkTS declarative syntax
- API keys stored in Constants.ets (placeholder, user fills in)
- All user-facing strings in Chinese

---

## File Structure

```
entry/src/main/ets/
├── pages/
│   ├── Index.ets           (modify) — Tab container
│   └── MovieDetail.ets     (create) — Movie detail page
├── view/
│   ├── HomeContent.ets     (create) — 首页 recommendation content
│   ├── DiscoverContent.ets (create) — 发现页 tag filter content
│   └── MineContent.ets     (create) — 我的 collection content
├── model/
│   └── Models.ets          (create) — Data interfaces
├── data/
│   ├── MovieRepository.ets (create) — TMDB API calls
│   └── EmotionMapper.ets   (create) — Emotion→genre mapping
├── viewmodel/
│   └── MovieViewModel.ets  (create) — Global state management
└── common/
    └── Constants.ets       (create) — TMDB config, genre list, colors
```

---

### Task 1: Foundation — Constants, Models, Emotion Mapper

**Files:**
- Create: `entry/src/main/ets/common/Constants.ets`
- Create: `entry/src/main/ets/model/Models.ets`
- Create: `entry/src/main/ets/data/EmotionMapper.ets`

**Interfaces:**
- Consumes: nothing
- Produces: Constants, Models, EmotionMapper types and maps used by all later tasks

- [ ] **Step 1: Write Constants.ets**

```typescript
// entry/src/main/ets/common/Constants.ets

export class Constants {
  static readonly TMDB_BASE_URL = 'https://api.themoviedb.org/3';
  static readonly TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p/w500';
  static readonly TMDB_API_KEY = 'YOUR_API_KEY_HERE'; // 用户替换
  static readonly LANG_ZH = 'zh-CN';

  // TMDB Genre ID mapping
  static readonly GENRES: Record<string, number> = {
    '动作': 28, '冒险': 12, '动画': 16, '喜剧': 35, '犯罪': 80,
    '纪录片': 99, '剧情': 18, '家庭': 10751, '奇幻': 14, '历史': 36,
    '恐怖': 27, '音乐': 10402, '悬疑': 9648, '爱情': 10749,
    '科幻': 878, '惊悚': 53, '战争': 10752, '西部': 37
  };

  static readonly GENRE_KEYS: string[] = Object.keys(Constants.GENRES);
}
```

- [ ] **Step 2: Write Models.ets**

```typescript
// entry/src/main/ets/model/Models.ets

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
```

- [ ] **Step 3: Write EmotionMapper.ets**

```typescript
// entry/src/main/ets/data/EmotionMapper.ets

import { EmotionItem } from '../model/Models';
import { Constants } from '../common/Constants';

export class EmotionMapper {
  static readonly EMOTIONS: EmotionItem[] = [
    {
      emoji: '😊', label: '开心', genreIds: [Constants.GENRES['喜剧']],
      minRating: 6.0, recText: '笑一笑，十年少！来点轻松愉快的～'
    },
    {
      emoji: '😢', label: '难过', genreIds: [Constants.GENRES['动画'], Constants.GENRES['家庭']],
      minRating: 7.0, recText: '让温暖的故事治愈你的心情。'
    },
    {
      emoji: '😤', label: '解压', genreIds: [Constants.GENRES['动作'], Constants.GENRES['惊悚']],
      minRating: 6.0, recText: '来点刺激的，把所有压力都释放掉！'
    },
    {
      emoji: '🔥', label: '燃', genreIds: [Constants.GENRES['动作'], Constants.GENRES['冒险']],
      minRating: 7.0, recText: '热血沸腾，燃到爆炸！'
    },
    {
      emoji: '💭', label: '治愈', genreIds: [Constants.GENRES['剧情'], Constants.GENRES['家庭']],
      minRating: 7.5, recText: '让一部好电影温柔地抱住你。'
    },
    {
      emoji: '😱', label: '刺激', genreIds: [Constants.GENRES['恐怖'], Constants.GENRES['惊悚']],
      minRating: 6.0, recText: '胆小鬼退散！今夜来点心跳加速的。'
    },
    {
      emoji: '🤔', label: '烧脑', genreIds: [Constants.GENRES['悬疑'], Constants.GENRES['科幻']],
      minRating: 7.0, recText: '准备好你的大脑，剧情反转再反转！'
    },
    {
      emoji: '🥰', label: '浪漫', genreIds: [Constants.GENRES['爱情']],
      minRating: 6.5, recText: '爱情电影永远不缺观众。'
    },
    {
      emoji: '😴', label: '放松', genreIds: [Constants.GENRES['纪录片']],
      minRating: 6.0, recText: '不用动脑子，静静享受就好。'
    },
    {
      emoji: '🎬', label: '随便看看', genreIds: [],
      minRating: 0, recText: '随机推荐，给你一点小惊喜！'
    }
  ];

  static getEmotionByLabel(label: string): EmotionItem | undefined {
    return EmotionMapper.EMOTIONS.find(e => e.label === label);
  }
}
```

---

### Task 2: TMDB Repository

**Files:**
- Create: `entry/src/main/ets/data/MovieRepository.ets`

**Interfaces:**
- Consumes: `Constants`, `Movie`, `MovieDetail` from Task 1
- Produces: `MovieRepository` class with fetch methods

- [ ] **Step 1: Write MovieRepository.ets**

```typescript
// entry/src/main/ets/data/MovieRepository.ets

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
```

---

### Task 3: Global State — Movie ViewModel

**Files:**
- Create: `entry/src/main/ets/viewmodel/MovieViewModel.ets`

**Interfaces:**
- Consumes: `CollectionState`, `Movie` from Task 1
- Produces: viewmodel singleton used by all content components and detail page

- [ ] **Step 1: Write MovieViewModel.ets**

```typescript
// entry/src/main/ets/viewmodel/MovieViewModel.ets

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
    const idx = this.collectionState.wantToWatch.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.wantToWatch.splice(idx, 1);
    } else {
      this.collectionState.wantToWatch.push(movieId);
    }
  }

  toggleWatched(movieId: number): void {
    const idx = this.collectionState.watched.indexOf(movieId);
    if (idx >= 0) {
      this.collectionState.watched.splice(idx, 1);
    } else {
      this.collectionState.watched.push(movieId);
    }
  }

  toggleLiked(movieId: number): void {
    const idx = this.collectionState.liked.indexOf(movieId);
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
```

---

### Task 4: Home Tab — Emotion Selector + Recommendation

**Files:**
- Create: `entry/src/main/ets/view/HomeContent.ets`

**Interfaces:**
- Consumes: `MovieRepository`, `EmotionMapper`, `MovieViewModel`, `Constants`
- Produces: `HomeContent` component with emotion selector, recommendation carousel, popular lists

- [ ] **Step 1: Write HomeContent.ets**

```typescript
// entry/src/main/ets/view/HomeContent.ets

import { Movie } from '../model/Models';
import { EmotionMapper } from '../data/EmotionMapper';
import { MovieRepository } from '../data/MovieRepository';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

@Component
export struct HomeContent {
  @State popularMovies: Movie[] = [];
  @State topRatedMovies: Movie[] = [];
  @State newMovies: Movie[] = [];
  @State emotionMovies: Movie[] = [];
  @State selectedEmotion: string = '';
  @State searchText: string = '';

  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();

  aboutToAppear() {
    this.loadData();
  }

  async loadData() {
    this.popularMovies = await this.repo.fetchPopular();
    this.topRatedMovies = await this.repo.fetchTopRated();
    this.newMovies = await this.repo.fetchNowPlaying();
  }

  async onEmotionSelect(emotionLabel: string) {
    this.selectedEmotion = emotionLabel;
    const emotion = EmotionMapper.getEmotionByLabel(emotionLabel);
    if (emotion) {
      if (emotion.genreIds.length > 0) {
        this.emotionMovies = await this.repo.fetchByGenre(emotion.genreIds);
        this.emotionMovies = this.emotionMovies.filter(m => m.voteAverage >= emotion.minRating);
      } else {
        this.emotionMovies = this.popularMovies.sort(() => Math.random() - 0.5);
      }
    }
  }

  clearEmotion() {
    this.selectedEmotion = '';
    this.emotionMovies = [];
  }

  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  onSearch() {
    if (this.searchText.trim()) {
      router.pushUrl({
        url: 'pages/Discover',
        params: { query: this.searchText.trim() }
      });
    }
  }

  build() {
    Column() {
      // 搜索栏
      Search({ placeholder: '搜索电影...', value: this.searchText })
        .width('100%')
        .onChange(v => this.searchText = v)
        .onSubmit(() => this.onSearch())

      Scroll() {
        Column() {
          // 情绪选择器
          Text('你现在是什么心情？')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ top: 16, left: 16 })

          if (this.selectedEmotion) {
            Row() {
              Text(`正在推荐 ${this.selectedEmotion} 电影`)
                .fontSize(14)
                .fontColor('#666')
              Blank()
              Text('清除')
                .fontSize(14)
                .fontColor('#1890ff')
                .onClick(() => this.clearEmotion())
            }
            .width('100%')
            .padding({ left: 16, right: 16 })
            .margin({ top: 8 })
          }

          Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.SpaceBetween }) {
            ForEach(EmotionMapper.EMOTIONS, (emotion: EmotionItem) => {
              Column() {
                Text(emotion.emoji).fontSize(28)
                Text(emotion.label).fontSize(12).margin({ top: 4 })
              }
              .width(64)
              .height(80)
              .justifyContent(FlexAlign.Center)
              .borderRadius(12)
              .backgroundColor(this.selectedEmotion === emotion.label ? '#e6f7ff' : '#f5f5f5')
              .onClick(() => this.onEmotionSelect(emotion.label))
            })
          }
          .width('100%')
          .padding(16)

          // 情绪推荐板块
          if (this.selectedEmotion && this.emotionMovies.length > 0) {
            Text(EmotionMapper.getEmotionByLabel(this.selectedEmotion)?.recText || '')
              .fontSize(14)
              .fontColor('#666')
              .margin({ left: 16, bottom: 8 })

            Swiper() {
              ForEach(this.emotionMovies, (movie: Movie) => {
                this.MovieCard({ movie: movie, onClick: () => this.goToDetail(movie.id) })
              })
            }
            .height(280)
            .indicator(true)
            .loop(false)
          }

          // 今日推荐
          Text('今日推荐')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Swiper() {
            ForEach(this.popularMovies.slice(0, 5), (movie: Movie) => {
              this.MovieCard({ movie: movie, onClick: () => this.goToDetail(movie.id) })
            })
          }
          .height(280)
          .indicator(true)
          .loop(true)

          // 热门榜单
          Text('近期热门')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll({ scroller: new Scroller() }) {
            Row() {
              ForEach(this.popularMovies, (movie: Movie) => {
                Column() {
                  Image(movie.posterPath)
                    .width(120)
                    .height(180)
                    .borderRadius(8)
                  Text(movie.title)
                    .width(120)
                    .fontSize(12)
                    .lineHeight(16)
                    .maxLines(2)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .margin({ top: 4 })
                }
                .margin({ right: 12 })
                .onClick(() => this.goToDetail(movie.id))
              })
            }
          }
          .scrollable(ScrollDirection.Horizontal)
          .margin({ left: 16 })

          // 高分经典
          Text('高分经典')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll({ scroller: new Scroller() }) {
            Row() {
              ForEach(this.topRatedMovies, (movie: Movie) => {
                Column() {
                  Image(movie.posterPath)
                    .width(120)
                    .height(180)
                    .borderRadius(8)
                  Text(movie.title)
                    .width(120)
                    .fontSize(12)
                    .lineHeight(16)
                    .maxLines(2)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .margin({ top: 4 })
                }
                .margin({ right: 12 })
                .onClick(() => this.goToDetail(movie.id))
              })
            }
          }
          .scrollable(ScrollDirection.Horizontal)
          .margin({ left: 16, bottom: 16 })

          // 新片速递
          Text('新片速递')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll({ scroller: new Scroller() }) {
            Row() {
              ForEach(this.newMovies, (movie: Movie) => {
                Column() {
                  Image(movie.posterPath)
                    .width(120)
                    .height(180)
                    .borderRadius(8)
                  Text(movie.title)
                    .width(120)
                    .fontSize(12)
                    .lineHeight(16)
                    .maxLines(2)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .margin({ top: 4 })
                }
                .margin({ right: 12 })
                .onClick(() => this.goToDetail(movie.id))
              })
            }
          }
          .scrollable(ScrollDirection.Horizontal)
          .margin({ left: 16, bottom: 16 })
        }
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }

  @Builder MovieCard({ movie, onClick }: { movie: Movie, onClick: () => void }) {
    Column() {
      Image(movie.posterPath)
        .width('100%')
        .height('100%')
        .objectFit(ImageFit.Cover)
      Text(movie.title)
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .fontColor('#fff')
        .position({ bottom: 40, left: 16 })
      Row() {
        Text(`${movie.voteAverage.toFixed(1)}`).fontSize(12).fontColor('#ffd700')
        Text(movie.releaseDate.slice(0, 4)).fontSize(12).fontColor('#fff').margin({ left: 8 })
      }
      .position({ bottom: 16, left: 16 })
    }
    .width('90%')
    .height(260)
    .borderRadius(16)
    .clip(true)
    .onClick(() => onClick())
  }
}
```

---

### Task 5: Discover Tab — Tag Filtering

**Files:**
- Create: `entry/src/main/ets/view/DiscoverContent.ets`

**Interfaces:**
- Consumes: `MovieRepository`, `Constants`, `MovieViewModel`, `Movie`
- Produces: `DiscoverContent` component with filter tags and grid results

- [ ] **Step 1: Write DiscoverContent.ets**

```typescript
// entry/src/main/ets/view/DiscoverContent.ets

import { Movie } from '../model/Models';
import { MovieRepository } from '../data/MovieRepository';
import { Constants } from '../common/Constants';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

@Component
export struct DiscoverContent {
  @State selectedGenres: number[] = [];
  @State minRating: number = 0;
  @State resultMovies: Movie[] = [];
  @State hasSearched: boolean = false;

  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();

  static readonly RATING_OPTIONS = [
    { label: '不限', value: 0 },
    { label: '6分+', value: 6 },
    { label: '7分+', value: 7 },
    { label: '8分+', value: 8 },
  ];

  toggleGenre(genreId: number) {
    const idx = this.selectedGenres.indexOf(genreId);
    if (idx >= 0) {
      this.selectedGenres.splice(idx, 1);
    } else {
      this.selectedGenres.push(genreId);
    }
  }

  async search() {
    this.hasSearched = true;
    this.resultMovies = await this.repo.fetchByFilters(this.selectedGenres, this.minRating);
  }

  clearFilters() {
    this.selectedGenres = [];
    this.minRating = 0;
    this.resultMovies = [];
    this.hasSearched = false;
  }

  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  build() {
    Column() {
      Scroll() {
        Column() {
          // 类型标签
          Text('类型').fontSize(16).fontWeight(FontWeight.Bold).margin({ top: 16, left: 16 })
          Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.Start }) {
            ForEach(Constants.GENRE_KEYS, (key: string) => {
              Text(key)
                .fontSize(14)
                .padding({ left: 16, right: 16, top: 8, bottom: 8 })
                .borderRadius(20)
                .backgroundColor(this.selectedGenres.indexOf(Constants.GENRES[key]) >= 0 ? '#1890ff' : '#f0f0f0')
                .fontColor(this.selectedGenres.indexOf(Constants.GENRES[key]) >= 0 ? '#fff' : '#333')
                .margin({ right: 8, bottom: 8 })
                .onClick(() => this.toggleGenre(Constants.GENRES[key]))
            })
          }
          .width('100%')
          .padding(16)

          // 评分筛选
          Text('评分').fontSize(16).fontWeight(FontWeight.Bold).margin({ left: 16 })
          Row() {
            ForEach(DiscoverContent.RATING_OPTIONS, (opt: { label: string, value: number }) => {
              Text(opt.label)
                .fontSize(14)
                .padding({ left: 16, right: 16, top: 8, bottom: 8 })
                .borderRadius(20)
                .backgroundColor(this.minRating === opt.value ? '#1890ff' : '#f0f0f0')
                .fontColor(this.minRating === opt.value ? '#fff' : '#333')
                .margin({ right: 8 })
                .onClick(() => this.minRating = opt.value)
            })
          }
          .margin({ left: 16, bottom: 16 })

          // 操作按钮
          Row() {
            Button('搜索').width(120).onClick(() => this.search())
            Button('清空').width(120).type(ButtonType.Normal).onClick(() => this.clearFilters())
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ bottom: 16 })

          // 结果
          if (this.hasSearched) {
            Text(`共找到 ${this.resultMovies.length} 部电影`)
              .fontSize(14)
              .fontColor('#999')
              .margin({ left: 16, bottom: 8 })
          }

          Grid() {
            ForEach(this.resultMovies, (movie: Movie) => {
              GridItem() {
                Column() {
                  Image(movie.posterPath)
                    .width('100%')
                    .height(200)
                    .borderRadius(8)
                    .objectFit(ImageFit.Cover)
                  Text(movie.title)
                    .fontSize(12)
                    .maxLines(2)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .margin({ top: 4 })
                  Row() {
                    Text(`${movie.voteAverage.toFixed(1)}`).fontSize(11).fontColor('#ffd700')
                    Text(movie.releaseDate.slice(0, 4)).fontSize(11).fontColor('#999').margin({ left: 4 })
                  }
                }
                .onClick(() => this.goToDetail(movie.id))
              }
            })
          }
          .columnsTemplate('1fr 1fr')
          .rowsTemplate('auto')
          .columnsGap(12)
          .rowsGap(12)
          .width('100%')
          .padding(16)
        }
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }
}
```

---

### Task 6: Mine Tab — Personal Collection

**Files:**
- Create: `entry/src/main/ets/view/MineContent.ets`

**Interfaces:**
- Consumes: `MovieViewModel`, `MovieRepository`, `Movie`
- Produces: `MineContent` component with 3 collection tabs

- [ ] **Step 1: Write MineContent.ets**

```typescript
// entry/src/main/ets/view/MineContent.ets

import { MovieViewModel } from '../viewmodel/MovieViewModel';
import { MovieRepository } from '../data/MovieRepository';
import { Movie } from '../model/Models';
import router from '@ohos.router';

@Component
export struct MineContent {
  @State currentTab: number = 0;
  @State wantMovies: Movie[] = [];
  @State watchedMovies: Movie[] = [];
  @State likedMovies: Movie[] = [];
  @State viewMode: string = 'grid';

  private vm: MovieViewModel = MovieViewModel.getInstance();
  private repo: MovieRepository = new MovieRepository();

  // 简化实现：展示收藏的 ID 列表，实际数据需要持久化存储
  getCurrentList(): number[] {
    const state = this.vm.getCollection();
    if (this.currentTab === 0) return state.wantToWatch;
    if (this.currentTab === 1) return state.watched;
    return state.liked;
  }

  getTabTitle(): string {
    if (this.currentTab === 0) return '想看';
    if (this.currentTab === 1) return '看过';
    return '喜欢';
  }

  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  build() {
    Column() {
      // 标题栏
      Row() {
        Text('我的').fontSize(24).fontWeight(FontWeight.Bold)
        Blank()
        Text(this.viewMode === 'grid' ? '列表' : '网格')
          .fontSize(14)
          .fontColor('#1890ff')
          .onClick(() => {
            this.viewMode = this.viewMode === 'grid' ? 'list' : 'grid';
          })
      }
      .width('100%')
      .padding(16)

      // Tab 切换
      Tabs({ index: this.currentTab }) {
        TabContent() {
          this.TabContentBuilder({ movies: this.wantMovies, tab: '想看' })
        }
        .tabBar('想看')
        TabContent() {
          this.TabContentBuilder({ movies: this.watchedMovies, tab: '看过' })
        }
        .tabBar('看过')
        TabContent() {
          this.TabContentBuilder({ movies: this.likedMovies, tab: '喜欢' })
        }
        .tabBar('喜欢')
      }
      .onChange(idx => this.currentTab = idx)
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }

  @Builder TabContentBuilder({ movies, tab }: { movies: Movie[], tab: string }) {
    if (movies.length === 0) {
      Text(`还没有${tab}的电影`)
        .fontSize(14)
        .fontColor('#999')
        .margin({ top: 100 })
        .width('100%')
        .textAlign(TextAlign.Center)
    } else {
      if (this.viewMode === 'grid') {
        Grid() {
          ForEach(movies, (movie: Movie) => {
            GridItem() {
              Column() {
                Image(movie.posterPath)
                  .width('100%')
                  .height(200)
                  .borderRadius(8)
                Text(movie.title).fontSize(12).margin({ top: 4 })
              }
              .onClick(() => this.goToDetail(movie.id))
            }
          })
        }
        .columnsTemplate('1fr 1fr')
        .columnsGap(12)
        .rowsGap(12)
        .width('100%')
        .padding(16)
      } else {
        List() {
          ForEach(movies, (movie: Movie) => {
            ListItem() {
              Row() {
                Image(movie.posterPath).width(60).height(90).borderRadius(6)
                Column() {
                  Text(movie.title).fontSize(14).fontWeight(FontWeight.Bold)
                  Text(movie.releaseDate.slice(0, 4)).fontSize(12).fontColor('#999')
                }
                .margin({ left: 12 })
                .alignItems(HorizontalAlign.Start)
                Blank()
              }
              .width('100%')
              .padding(8)
              .onClick(() => this.goToDetail(movie.id))
            }
          })
        }
        .width('100%')
      }
    }
  }
}
```

---

### Task 7: Movie Detail Page

**Files:**
- Create: `entry/src/main/ets/pages/MovieDetail.ets`
- Modify: `entry/src/main/resources/base/profile/main_pages.json`

**Interfaces:**
- Consumes: `MovieRepository`, `MovieViewModel`, `MovieDetail`
- Produces: full detail page navigated from any tab

- [ ] **Step 1: Create MovieDetail.ets**

```typescript
// entry/src/main/ets/pages/MovieDetail.ets

import { MovieDetail, Movie } from '../model/Models';
import { MovieRepository } from '../data/MovieRepository';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

@Entry
@Component
struct MovieDetailPage {
  @State movie: MovieDetail | null = null;
  @State movieId: number = 0;

  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();

  aboutToAppear() {
    const params = router.getParams() as Record<string, Object>;
    this.movieId = params['movieId'] as number;
    this.loadDetail();
  }

  async loadDetail() {
    this.movie = await this.repo.fetchMovieDetail(this.movieId);
  }

  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  build() {
    Column() {
      if (this.movie) {
        Scroll() {
          Column() {
            // 海报背景
            Stack() {
              Image(this.movie.backdropPath || this.movie.posterPath)
                .width('100%')
                .height(300)
                .objectFit(ImageFit.Cover)
                .blur(10)
              Image(this.movie.posterPath)
                .width(150)
                .height(225)
                .borderRadius(12)
                .objectFit(ImageFit.Cover)
            }
            .width('100%')
            .height(300)

            // 基本信息
            Text(this.movie.title)
              .fontSize(22)
              .fontWeight(FontWeight.Bold)
              .margin({ top: 16, left: 16 })
              .width('100%')

            Row() {
              Text(this.movie.releaseDate.slice(0, 4))
              if (this.movie.runtime > 0) {
                Text(`${Math.floor(this.movie.runtime / 60)}h${this.movie.runtime % 60}m`)
                  .margin({ left: 12 })
              }
              Text(`${this.movie.voteAverage.toFixed(1)}`)
                .margin({ left: 12 })
                .fontColor('#ffd700')
            }
            .fontSize(14)
            .fontColor('#666')
            .margin({ left: 16, top: 8 })
            .width('100%')

            // 类型标签
            if (this.movie.genreNames.length > 0) {
              Flex({ wrap: FlexWrap.Wrap }) {
                ForEach(this.movie.genreNames, (name: string) => {
                  Text(name)
                    .fontSize(12)
                    .padding({ left: 12, right: 12, top: 4, bottom: 4 })
                    .borderRadius(12)
                    .backgroundColor('#f0f0f0')
                    .margin({ right: 8, top: 8 })
                })
              }
              .margin({ left: 16, top: 8 })
              .width('100%')
            }

            // 推荐理由
            if (this.movie.director) {
              Text(`推荐理由：由${this.movie.director}执导的作品，不容错过！`)
                .fontSize(14)
                .fontColor('#1890ff')
                .margin({ left: 16, top: 16, right: 16 })
                .width('100%')
            }

            // 操作按钮
            Row() {
              Button('想看')
                .fontColor(this.vm.isWantToWatch(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isWantToWatch(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .onClick(() => this.vm.toggleWantToWatch(this.movie!.id))
              Button('看过')
                .fontColor(this.vm.isWatched(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isWatched(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .margin({ left: 12 })
                .onClick(() => this.vm.toggleWatched(this.movie!.id))
              Button('喜欢')
                .fontColor(this.vm.isLiked(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isLiked(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .margin({ left: 12 })
                .onClick(() => this.vm.toggleLiked(this.movie!.id))
            }
            .margin({ top: 16 })
            .justifyContent(FlexAlign.Center)

            // 剧情简介
            if (this.movie.overview) {
              Text('剧情简介')
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .margin({ left: 16, top: 24 })
                .width('100%')
              Text(this.movie.overview)
                .fontSize(14)
                .fontColor('#333')
                .lineHeight(22)
                .margin({ left: 16, top: 8, right: 16 })
                .width('100%')
            }

            // 演员表
            if (this.movie.cast.length > 0) {
              Text('演员')
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .margin({ left: 16, top: 24, bottom: 8 })
                .width('100%')

              Scroll({ scroller: new Scroller() }) {
                Row() {
                  ForEach(this.movie.cast, (actor: CastMember) => {
                    Column() {
                      Image(actor.profilePath || '')
                        .width(80)
                        .height(80)
                        .borderRadius(40)
                        .objectFit(ImageFit.Cover)
                        .backgroundColor('#f0f0f0')
                      Text(actor.name).fontSize(12).margin({ top: 4 }).maxLines(2)
                      Text(actor.character).fontSize(10).fontColor('#999')
                    }
                    .width(90)
                    .margin({ right: 12 })
                  })
                }
              }
              .scrollable(ScrollDirection.Horizontal)
              .margin({ left: 16 })
            }

            // 相似推荐
            if (this.movie.recommendations.length > 0) {
              Text('相似推荐')
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .margin({ left: 16, top: 24, bottom: 8 })
                .width('100%')

              Scroll({ scroller: new Scroller() }) {
                Row() {
                  ForEach(this.movie.recommendations, (rec: Movie) => {
                    Column() {
                      Image(rec.posterPath)
                        .width(120)
                        .height(180)
                        .borderRadius(8)
                      Text(rec.title)
                        .width(120)
                        .fontSize(12)
                        .maxLines(2)
                        .textOverflow({ overflow: TextOverflow.Ellipsis })
                        .margin({ top: 4 })
                    }
                    .margin({ right: 12 })
                    .onClick(() => this.goToDetail(rec.id))
                  })
                }
              }
              .scrollable(ScrollDirection.Horizontal)
              .margin({ left: 16, bottom: 24 })
            }
          }
          .width('100%')
        }
      } else {
        Text('加载中...').margin({ top: 200 }).width('100%').textAlign(TextAlign.Center)
      }

      // 返回按钮
      Button('返回')
        .position({ bottom: 30 })
        .width(200)
        .onClick(() => router.back())
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }
}
```

- [ ] **Step 2: Update main_pages.json**

Add MovieDetail page:

```json
{
  "src": [
    "pages/Index",
    "pages/MovieDetail"
  ]
}
```

---

### Task 8: Main Tab Container — Index.ets

**Files:**
- Modify: `entry/src/main/ets/pages/Index.ets`

**Interfaces:**
- Consumes: `HomeContent`, `DiscoverContent`, `MineContent`
- Produces: Tab container with 3 tabs

- [ ] **Step 1: Rewrite Index.ets**

```typescript
// entry/src/main/ets/pages/Index.ets

import { HomeContent } from '../view/HomeContent';
import { DiscoverContent } from '../view/DiscoverContent';
import { MineContent } from '../view/MineContent';

@Entry
@Component
struct Index {
  @State currentIndex: number = 0;

  build() {
    Tabs({ index: this.currentIndex }) {
      TabContent() {
        HomeContent()
      }
      .tabBar(this.TabBuilder({ icon: '🏠', text: '首页', index: 0 }))

      TabContent() {
        DiscoverContent()
      }
      .tabBar(this.TabBuilder({ icon: '🔍', text: '发现', index: 1 }))

      TabContent() {
        MineContent()
      }
      .tabBar(this.TabBuilder({ icon: '👤', text: '我的', index: 2 }))
    }
    .vertical(false)
    .barMode(BarMode.Fixed)
    .onChange(idx => this.currentIndex = idx)
    .width('100%')
    .height('100%')
  }

  @Builder TabBuilder({ icon, text, index }: { icon: string, text: string, index: number }) {
    Column() {
      Text(icon).fontSize(20)
      Text(text).fontSize(10).margin({ top: 2 })
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .fontColor(this.currentIndex === index ? '#1890ff' : '#999')
  }
}
```

---

## Self-Review

1. **Spec coverage:** All spec requirements covered — emotion recommendations (Task 4), tag filtering (Task 5), collection management (Task 6), movie detail with poster/cast/similar (Task 7), tab navigation (Task 8).
2. **Placeholder scan:** No TBD, TODO, or incomplete sections. All code complete.
3. **Type consistency:** `Movie`, `MovieDetail`, `EmotionItem`, `CastMember`, `CollectionState` types used consistently across all files.
4. **Scope check:** Focused single app, no decomposition needed.
