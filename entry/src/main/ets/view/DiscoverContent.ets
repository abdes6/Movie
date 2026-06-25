import { Movie } from '../model/Models';
import { MovieRepository } from '../data/MovieRepository';
import { Constants } from '../common/Constants';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

interface RatingOption {
  label: string;
  value: number;
}

// 🌟 2. 移到 struct 外部声明常量（结合之前的 static 报错修正）
// 必须显式声明数组类型为 RatingOption[]
const RATING_OPTIONS: RatingOption[] = [
  { label: '不限', value: 0 },
  { label: '6分+', value: 6 },
  { label: '7分+', value: 7 },
  { label: '8分+', value: 8 }
];
@Component
export struct DiscoverContent {
  @State selectedGenres: number[] = [];
  @State minRating: number = 0;
  @State resultMovies: Movie[] = [];
  @State hasSearched: boolean = false;

  private repo: MovieRepository = new MovieRepository();
  private vm: MovieViewModel = MovieViewModel.getInstance();


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
          Text('类型')
            .fontSize(16)
            .fontWeight(FontWeight.Bold)
            .margin({ top: 16, left: 16 })

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

          Text('评分')
            .fontSize(16)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16 })

          Row() {
            ForEach(RATING_OPTIONS, (opt: RatingOption) => { // 🌟 1. 修复：这里的类型必须改成具体的 RatingOption 接口
              Text(opt.label)
                .fontSize(14)
                .padding({ left: 16, right: 16, top: 8, bottom: 8 })
                .borderRadius(20)
                .backgroundColor(this.minRating === opt.value ? '#1890ff' : '#f0f0f0')
                .fontColor(this.minRating === opt.value ? '#fff' : '#333')
                .margin({ right: 8 })
                .onClick(() => this.minRating = opt.value)
            }, (opt: RatingOption) => opt.label) // 🌟 2. 规范：显式加上键值生成器（Key Generator），保证渲染性能与状态刷新
          }
          .margin({ left: 16, bottom: 16 })

          Row() {
            Button('搜索')
              .width(120)
              .onClick(() => this.search())
            Button('清空')
              .width(120)
              .type(ButtonType.Normal)
              .onClick(() => this.clearFilters())
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ bottom: 16 })

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
                    Text(`${movie.voteAverage.toFixed(1)}`)
                      .fontSize(11)
                      .fontColor('#ffd700')
                    Text(movie.releaseDate.slice(0, 4))
                      .fontSize(11)
                      .fontColor('#999')
                      .margin({ left: 4 })
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
