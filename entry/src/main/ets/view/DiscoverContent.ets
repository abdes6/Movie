// 发现页组件：按类型 + 评分的组合筛选
import { Movie } from '../model/Models';
import { MovieRepository } from '../data/MovieRepository';
import { Constants } from '../common/Constants';
import { MovieViewModel } from '../viewmodel/MovieViewModel';
import router from '@ohos.router';

interface RatingOption {
  label: string;
  value: number;
}

// 评分筛选项
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

  // 切换类型标签的选中状态
  toggleGenre(genreId: number): void {
    const idx: number = this.selectedGenres.indexOf(genreId);
    if (idx >= 0) {
      this.selectedGenres.splice(idx, 1);
    } else {
      this.selectedGenres.push(genreId);
    }
  }

  // 执行搜索
  async search(): Promise<void> {
    this.hasSearched = true;
    this.resultMovies = await this.repo.fetchByFilters(this.selectedGenres, this.minRating);
  }

  // 清空所有筛选条件
  clearFilters(): void {
    this.selectedGenres = [];
    this.minRating = 0;
    this.resultMovies = [];
    this.hasSearched = false;
  }

  goToDetail(movieId: number): void {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  build() {
    Column() {
      Scroll() {
        Column() {
          // --- 类型筛选 ---
          Text('类型')
            .fontSize(16)
            .fontWeight(FontWeight.Bold)
            .margin({ top: 16, left: 16 })

          Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.Start }) {
            ForEach(Constants.GENRE_KEYS, (key: string): void => {
              Text(key)
                .fontSize(14)
                .padding({ left: 16, right: 16, top: 8, bottom: 8 })
                .borderRadius(20)
                .backgroundColor(this.selectedGenres.indexOf(Constants.GENRES[key]) >= 0 ? '#1890ff' : '#f0f0f0')
                .fontColor(this.selectedGenres.indexOf(Constants.GENRES[key]) >= 0 ? '#fff' : '#333')
                .margin({ right: 8, bottom: 8 })
                .onClick((): void => {
                  this.toggleGenre(Constants.GENRES[key]);
                })
            }, (key: string): string => key)
          }
          .width('100%')
          .padding(16)

          // --- 评分筛选 ---
          Text('评分')
            .fontSize(16)
            .fontWeight(FontWeight.Bold)
            .margin({ left: 16 })

          Row() {
            ForEach(RATING_OPTIONS, (opt: RatingOption): void => {
              Text(opt.label)
                .fontSize(14)
                .padding({ left: 16, right: 16, top: 8, bottom: 8 })
                .borderRadius(20)
                .backgroundColor(this.minRating === opt.value ? '#1890ff' : '#f0f0f0')
                .fontColor(this.minRating === opt.value ? '#fff' : '#333')
                .margin({ right: 8 })
                .onClick((): void => {
                  this.minRating = opt.value;
                })
            }, (opt: RatingOption): string => opt.label)
          }
          .margin({ left: 16, bottom: 16 })

          // --- 操作按钮 ---
          Row() {
            Button('搜索')
              .width(120)
              .onClick((): void => {
                this.search();
              })
            Button('清空')
              .width(120)
              .type(ButtonType.Normal)
              .onClick((): void => {
                this.clearFilters();
              })
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ bottom: 16 })

          // --- 结果统计 ---
          if (this.hasSearched) {
            Text(`共找到 ${this.resultMovies.length} 部电影`)
              .fontSize(14)
              .fontColor('#999')
              .margin({ left: 16, bottom: 8 })
          }

          // --- 结果网格（2列） ---
          Grid() {
            ForEach(this.resultMovies, (movie: Movie): void => {
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
                .onClick((): void => {
                  this.goToDetail(movie.id);
                })
              }
            }, (movie: Movie): string => movie.id.toString())
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
