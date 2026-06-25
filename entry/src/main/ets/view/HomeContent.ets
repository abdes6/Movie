// 数据模型导入
import { Movie } from '../model/Models';
import { EmotionItem } from '../model/Models';
// 数据层导入
import { EmotionMapper } from '../data/EmotionMapper';
import { MovieRepository } from '../data/MovieRepository';
// 全局状态管理
import { MovieViewModel } from '../viewmodel/MovieViewModel';
// 路由跳转
import router from '@ohos.router';

// 电影卡片组件参数接口
interface MovieCardParam {
  movie: Movie;
  onClick: () => void;
}

// 首页内容组件：情绪推荐 + 榜单浏览 + 搜索入口
@Component
export struct HomeContent {
  // 数据状态：热门 / 高分 / 新片 / 情绪推荐 / 选中情绪 / 搜索文本
  @State popularMovies: Movie[] = [];
  @State topRatedMovies: Movie[] = [];
  @State newMovies: Movie[] = [];
  @State emotionMovies: Movie[] = [];
  @State selectedEmotion: string = '';
  @State searchText: string = '';

  // 数据仓库与状态管理实例
  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();

  // 页面初始化：加载三个榜单数据
  aboutToAppear() {
    this.loadData();
  }

  // 异步加载热门、高分、新片数据
  async loadData() {
    this.popularMovies = await this.repo.fetchPopular();
    this.topRatedMovies = await this.repo.fetchTopRated();
    this.newMovies = await this.repo.fetchNowPlaying();
  }

  // 情绪选择回调：根据情绪映射获取电影推荐
  async onEmotionSelect(emotionLabel: string) {
    this.selectedEmotion = emotionLabel;
    const emotion = EmotionMapper.getEmotionByLabel(emotionLabel);
    if (emotion) {
      if (emotion.genreIds.length > 0) {
        // 按类型获取 + 评分过滤
        this.emotionMovies = await this.repo.fetchByGenre(emotion.genreIds);
        this.emotionMovies = this.emotionMovies.filter(m => m.voteAverage >= emotion.minRating);
      } else {
        // 无类型映射（如"随便看看"）：随机打乱热门列表
        this.emotionMovies = this.popularMovies.sort(() => Math.random() - 0.5);
      }
    }
  }

  // 清除情绪筛选，恢复默认推荐
  clearEmotion() {
    this.selectedEmotion = '';
    this.emotionMovies = [];
  }

  // 跳转到电影详情页
  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  // 搜索提交：跳转到详情页（搜索结果待 V2 实现独立搜索页）
  onSearch() {
    if (this.searchText.trim()) {
      router.pushUrl({
        url: 'pages/MovieDetail',
        params: { query: this.searchText.trim() }
      });
    }
  }

  // 首页 UI 构建
  build() {
    Column() {
      // 顶部搜索栏
      Search({ placeholder: '搜索电影...', value: this.searchText })
        .width('100%')
        .onChange(v => this.searchText = v)
        .onSubmit(() => this.onSearch())

      // 可滚动内容区域
      Scroll() {
        Column() {
          // ====== 情绪选择区域 ======
          Text('你现在是什么心情？')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ top: 16, left: 16 })

          // 已选情绪时的提示行
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

          // 10 种情绪图标网格
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

          // ====== 情绪推荐结果轮播 ======
          if (this.selectedEmotion && this.emotionMovies.length > 0) {
            Text(EmotionMapper.getEmotionByLabel(this.selectedEmotion)?.recText || '')
              .fontSize(14)
              .fontColor('#666')
              .margin({ left: 16, bottom: 8 })

            Swiper() {
              ForEach(this.emotionMovies, (movie: Movie) => {
                this.MovieCard({ movie: movie, onClick: ():void => this.goToDetail(movie.id) })
              })
            }
            .height(280)
            .indicator(true)
            .loop(false)
          }

          // ====== 今日推荐（热门榜轮播） ======
          Text('今日推荐')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Swiper() {
            ForEach(this.popularMovies.slice(0, 5), (movie: Movie) => {
              this.MovieCard({ movie: movie, onClick: ():void => this.goToDetail(movie.id) })
            })
          }
          .height(280)
          .indicator(true)
          .loop(true)

          // ====== 近期热门（横向滚动列表） ======
          Text('近期热门')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
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

          // ====== 高分经典（横向滚动列表） ======
          Text('高分经典')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
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
          .margin({ left: 16 })

          // ====== 新片速递（横向滚动列表） ======
          Text('新片速递')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16, top: 16, bottom: 8 })

          Scroll(new Scroller()) {
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

  // 电影卡片组件：海报 + 标题 + 评分 + 年份
  @Builder MovieCard(param: MovieCardParam) {
    Column() {
      // 电影海报背景
      Image(param.movie.posterPath)
        .width('100%')
        .height('100%')
        .objectFit(ImageFit.Cover)
      // 电影标题（叠加在海报底部上方）
      Text(param.movie.title)
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .fontColor('#fff')
        .position({ bottom: 40, left: 16 })
      // 评分 + 年份（叠加在海报底部）
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
    .onClick(() => param.onClick())
  }
}
