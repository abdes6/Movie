// 首页内容组件：搜索 + 情绪推荐 + 今日推荐 + 榜单
import { Movie } from '../model/Models';
import { EmotionItem } from '../model/Models';
import { EmotionMapper } from '../data/EmotionMapper';
import { MovieRepository } from '../data/MovieRepository';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

interface MovieCardParam {
  movie: Movie;
  onClick: () => void;
}

@Component
export struct HomeContent {
  // --- 数据状态 ---
  @State popularMovies: Movie[] = [];
  @State topRatedMovies: Movie[] = [];
  @State newMovies: Movie[] = [];
  @State emotionMovies: Movie[] = [];
  @State selectedEmotion: string = '';
  @State searchText: string = '';

  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();

  // 组件挂载时加载首页数据
  aboutToAppear(): void {
    this.loadData();
  }

  // 同时加载热门、高分、正在上映三类数据
  async loadData(): Promise<void> {
    this.popularMovies = await this.repo.fetchPopular();
    this.topRatedMovies = await this.repo.fetchTopRated();
    this.newMovies = await this.repo.fetchNowPlaying();
  }

  // 用户选择情绪后触发的推荐逻辑
  async onEmotionSelect(emotionLabel: string): Promise<void> {
    this.selectedEmotion = emotionLabel;
    const emotion: EmotionItem | undefined = EmotionMapper.getEmotionByLabel(emotionLabel);
    if (emotion) {
      if (emotion.genreIds.length > 0) {
        // 按情绪的 genreIds 请求后端 discover 接口
        this.emotionMovies = await this.repo.fetchByGenre(emotion.genreIds);
        this.emotionMovies = this.emotionMovies.filter((m: Movie): boolean => m.voteAverage >= emotion.minRating);
      } else {
        // "随便看看"：从热门列表中随机排序取
        this.emotionMovies = this.popularMovies.sort((): number => Math.random() - 0.5);
      }
    }
  }

  // 清除情绪选择
  clearEmotion(): void {
    this.selectedEmotion = '';
    this.emotionMovies = [];
  }

  // 跳转到电影详情页
  goToDetail(movieId: number): void {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  // 搜索：输入关键词后跳转（当前直接跳详情页，非搜索结果页）
  onSearch(): void {
    if (this.searchText.trim()) {
      router.pushUrl({
        url: 'pages/MovieDetail',
        params: { query: this.searchText.trim() }
      });
    }
  }

  build() {
    Column() {
      // --- 搜索栏 ---
      Search({ placeholder: '搜索电影...', value: this.searchText })
        .width('100%')
        .onChange((v: string): void => {
          this.searchText = v;
        })
        .onSubmit((): void => {
          this.onSearch();
        })

      // --- 内容区域（可滚动） ---
      Scroll() {
        Column() {
          // --- 情绪入口 ---
          Text('你现在是什么心情？')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ top: 16, left: 16 })

          // 已选情绪时的提示和清除按钮
          if (this.selectedEmotion) {
            Row() {
              Text(`正在推荐 ${this.selectedEmotion} 电影`)
                .fontSize(14)
                .fontColor('#666')
              Blank()
              Text('清除')
                .fontSize(14)
                .fontColor('#1890ff')
                .onClick((): void => {
                  this.clearEmotion();
                })
            }
            .width('100%')
            .padding({ left: 16, right: 16 })
            .margin({ top: 8 })
          }

          // 10 种情绪按钮网格
          Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.SpaceBetween }) {
            ForEach(EmotionMapper.EMOTIONS, (emotion: EmotionItem): void => {
              Column() {
                Text(emotion.emoji).fontSize(28)
                Text(emotion.label).fontSize(12).margin({ top: 4 })
              }
              .width(64)
              .height(80)
              .justifyContent(FlexAlign.Center)
              .borderRadius(12)
              .backgroundColor(this.selectedEmotion === emotion.label ? '#e6f7ff' : '#f5f5f5')
              .onClick((): void => {
                this.onEmotionSelect(emotion.label);
              })
            }, (emotion: EmotionItem): string => emotion.label)
          }
          .width('100%')
          .padding(16)

          // --- 情绪推荐结果（横向轮播） ---
          if (this.selectedEmotion && this.emotionMovies.length > 0) {
            Text(EmotionMapper.getEmotionByLabel(this.selectedEmotion)?.recText || '')
              .fontSize(14)
              .fontColor('#666')
              .margin({ left: 16, bottom: 8 })

            Swiper() {
              ForEach(this.emotionMovies, (movie: Movie): void => {
                this.MovieCard({ movie: movie, onClick: (): void => this.goToDetail(movie.id) })
              }, (movie: Movie): string => movie.id.toString())
            }
            .height(280)
            .indicator(true)
            .loop(false)
          }

          // --- 今日推荐（轮播） ---
          Text('今日推荐')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Swiper() {
            ForEach(this.popularMovies.slice(0, 5), (movie: Movie): void => {
              this.MovieCard({ movie: movie, onClick: (): void => this.goToDetail(movie.id) })
            }, (movie: Movie): string => movie.id.toString())
          }
          .height(280)
          .indicator(true)
          .loop(true)

          // --- 近期热门（横向滚动列表） ---
          Text('近期热门')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
            Row() {
              ForEach(this.popularMovies, (movie: Movie): void => {
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
                .onClick((): void => {
                  this.goToDetail(movie.id);
                })
              }, (movie: Movie): string => movie.id.toString())
            }
          }
          .scrollable(ScrollDirection.Horizontal)
          .margin({ left: 16 })

          // --- 高分经典（横向滚动列表） ---
          Text('高分经典')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
            Row() {
              ForEach(this.topRatedMovies, (movie: Movie): void => {
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
                .onClick((): void => {
                  this.goToDetail(movie.id);
                })
              }, (movie: Movie): string => movie.id.toString())
            }
          }
          .scrollable(ScrollDirection.Horizontal)
          .margin({ left: 16 })

          // --- 新片速递（横向滚动列表） ---
          Text('新片速递')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
            Row() {
              ForEach(this.newMovies, (movie: Movie): void => {
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
                .onClick((): void => {
                  this.goToDetail(movie.id);
                })
              }, (movie: Movie): string => movie.id.toString())
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

  // 电影卡片（用于轮播展示）：海报铺满 + 底部标题/评分叠加
  @Builder MovieCard(param: MovieCardParam) {
    Column() {
      Image(param.movie.posterPath)
        .width('100%')
        .height('100%')
        .objectFit(ImageFit.Cover)
      // 标题（叠加在海报底部）
      Text(param.movie.title)
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .fontColor('#fff')
        .position({ bottom: 40, left: 16 })
      Row() {
        Text(`${param.movie.voteAverage.toFixed(1)}`)
          .fontSize(12)
          .fontColor('#ffd700')
        Text(param.movie.releaseDate.slice(0, 4))
          .fontSize(12)
          .fontColor('#fff')
          .margin({ left: 8 })
      }
      .position({ bottom: 16, left: 16 })
    }
    .width('90%')
    .height(260)
    .borderRadius(16)
    .clip(true)
    .onClick((): void => param.onClick())
  }
}
