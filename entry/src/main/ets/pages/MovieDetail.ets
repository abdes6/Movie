// 数据模型导入
import { MovieDetail, Movie, CastMember } from '../model/Models';
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

  // 页面初始化：从路由参数获取电影ID并加载数据
  aboutToAppear() {
    const params = router.getParams() as Record<string, Object>;
    this.movieId = params['movieId'] as number;
    this.loadDetail();
  }

  // 异步加载电影详情数据，含异常处理
  async loadDetail() {
    try {
      this.movie = await this.repo.fetchMovieDetail(this.movieId);
    } catch (e) {
      console.error('Failed to load movie detail:', JSON.stringify(e));
    }
  }

  // 跳转到另一部电影的详情页（用于相似推荐）
  goToDetail(movieId: number) {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }


  build() {
    Column() {
      if (this.movie) {
        Scroll() {
          Column() {
            // 顶部海报区域：背景模糊大图 + 前景正片海报
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

            // 电影标题
            Text(this.movie.title)
              .fontSize(22)
              .fontWeight(FontWeight.Bold)
              .margin({ top: 16, left: 16 })
              .width('100%')

            // 基本信息行：年份、时长、评分
            Row() {
              Text(this.movie.releaseDate.slice(0, 4))
                .fontSize(14)
                .fontColor('#666')
              if (this.movie.runtime > 0) {
                Text(`${Math.floor(this.movie.runtime / 60)}h${this.movie.runtime % 60}m`)
                  .fontSize(14)
                  .fontColor('#666')
                  .margin({ left: 12 })
              }
              Text(`${this.movie.voteAverage.toFixed(1)}`)
                .fontSize(14)
                .fontColor('#ffd700')
                .margin({ left: 12 })
            }
            .margin({ left: 16, top: 8 })
            .width('100%')

            // 类型标签组
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

            // 推荐理由：基于导演信息的动态文案
            if (this.movie.director) {
              Text(`推荐理由：由${this.movie.director}执导的作品，不容错过！`)
                .fontSize(14)
                .fontColor('#1890ff')
                .margin({ left: 16, top: 16, right: 16 })
                .width('100%')
            }

            // 操作按钮行：想看 / 看过 / 喜欢
            Row() {
              Button('想看')
                .fontColor(this.vm.isWantToWatch(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isWantToWatch(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .onClick(() => this.vm.toggleWantToWatch(this.movieId))
              Button('看过')
                .fontColor(this.vm.isWatched(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isWatched(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .margin({ left: 12 })
                .onClick(() => this.vm.toggleWatched(this.movieId))
              Button('喜欢')
                .fontColor(this.vm.isLiked(this.movie.id) ? '#1890ff' : '#666')
                .backgroundColor(this.vm.isLiked(this.movie.id) ? '#e6f7ff' : '#f5f5f5')
                .margin({ left: 12 })
                .onClick(() => this.vm.toggleLiked(this.movieId))
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

            // 演员列表：横向滑动
            if (this.movie.cast.length > 0) {
              Text('演员')
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .margin({ left: 16, top: 24, bottom: 8 })
                .width('100%')

              Scroll(new Scroller()) {
                Row() {
                  ForEach(this.movie.cast, (actor: CastMember) => {
                    Column() {
                      Image(actor.profilePath || '')
                        .width(80)
                        .height(80)
                        .borderRadius(40)
                        .objectFit(ImageFit.Cover)
                        .backgroundColor('#f0f0f0')
                      Text(actor.name)
                        .fontSize(12)
                        .margin({ top: 4 })
                        .maxLines(2)
                      Text(actor.character)
                        .fontSize(10)
                        .fontColor('#999')
                    }
                    .width(90)
                    .margin({ right: 12 })
                  })
                }
              }
              .scrollable(ScrollDirection.Horizontal)
              .margin({ left: 16 })
            }

            // 相似推荐：横向滑动，点击跳转详情
            if (this.movie.recommendations.length > 0) {
              Text('相似推荐')
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .margin({ left: 16, top: 24, bottom: 8 })
                .width('100%')

              Scroll(new Scroller()) {
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
        .layoutWeight(1)
      } else {
        // 数据未加载完成时展示加载提示
        Text('加载中...')
          .margin({ top: 200 })
          .width('100%')
          .textAlign(TextAlign.Center)
          .layoutWeight(1)
      }

      // 底部固定返回按钮
      Button('返回')
        .width(200)
        .margin({ bottom: 24 })
        .alignSelf(ItemAlign.Center)
        .onClick(() => router.back())
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }
}
