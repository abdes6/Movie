import { MovieViewModel } from '../viewmodel/MovieViewModel';
import { MovieRepository } from '../data/MovieRepository';
import { Movie } from '../model/Models';
import router from '@ohos.router';

interface TabContentParam {
  movies: Movie[];
  tab: string;
}

@Component
export struct MineContent {
  @State currentTab: number = 0;
  @State wantMovies: Movie[] = [];
  @State watchedMovies: Movie[] = [];
  @State likedMovies: Movie[] = [];
  @State viewMode: string = 'grid';

  private vm: MovieViewModel = MovieViewModel.getInstance();
  private repo: MovieRepository = new MovieRepository();

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
      Row() {
        Text('我的')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
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

  @Builder TabContentBuilder(param: TabContentParam) {
    if (param.movies.length === 0) {
      Text(`还没有${param.tab}的电影`)
        .fontSize(14)
        .fontColor('#999')
        .margin({ top: 100 })
        .width('100%')
        .textAlign(TextAlign.Center)
    } else {
      if (this.viewMode === 'grid') {
        Grid() {
          ForEach(param.movies, (movie: Movie) => {
            GridItem() {
              Column() {
                Image(movie.posterPath)
                  .width('100%')
                  .height(200)
                  .borderRadius(8)
                Text(movie.title)
                  .fontSize(12)
                  .margin({ top: 4 })
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
          ForEach(param.movies, (movie: Movie) => {
            ListItem() {
              Row() {
                Image(movie.posterPath)
                  .width(60)
                  .height(90)
                  .borderRadius(6)
                Column() {
                  Text(movie.title)
                    .fontSize(14)
                    .fontWeight(FontWeight.Bold)
                  Text(movie.releaseDate.slice(0, 4))
                    .fontSize(12)
                    .fontColor('#999')
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
