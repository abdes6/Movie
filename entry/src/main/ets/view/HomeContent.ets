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
        url: 'pages/MovieDetail',
        params: { query: this.searchText.trim() }
      });
    }
  }

  build() {
    Column() {
      Search({ placeholder: '搜索电影...', value: this.searchText })
        .width('100%')
        .onChange(v => this.searchText = v)
        .onSubmit(() => this.onSearch())

      Scroll() {
        Column() {
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

  @Builder MovieCard(param: MovieCardParam) {
    Column() {
      Image(param.movie.posterPath)
        .width('100%')
        .height('100%')
        .objectFit(ImageFit.Cover)
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
    .onClick(() => param.onClick())
  }
}
