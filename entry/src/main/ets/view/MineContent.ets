// "我的"页面组件：想看/看过/喜欢三个分类 Tab + 网格/列表模式切换
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

  // 获取当前 Tab 对应的收藏 ID 列表
  getCurrentList(): number[] {
    const state = this.vm.getCollection();
    if (this.currentTab === 0) return state.wantToWatch;
    if (this.currentTab === 1) return state.watched;
    return state.liked;
  }

  // 获取当前 Tab 标题
  getTabTitle(): string {
    if (this.currentTab === 0) return '想看';
    if (this.currentTab === 1) return '看过';
    return '喜欢';
  }

  goToDetail(movieId: number): void {
    router.pushUrl({ url: 'pages/MovieDetail', params: { movieId: movieId } });
  }

  build() {
    Column() {
      // --- 顶部标题栏 + 视图切换 ---
      Row() {
        Text('我的')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
        Blank()
        Text(this.viewMode === 'grid' ? '列表' : '网格')
          .fontSize(14)
          .fontColor('#1890ff')
          .onClick((): void => {
            this.viewMode = this.viewMode === 'grid' ? 'list' : 'grid';
          })
      }
      .width('100%')
      .padding(16)

      // --- 三个收藏分类 Tab ---
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
      .onChange((idx: number): void => {
        this.currentTab = idx;
      })
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff')
  }

  // 收藏内容的展示模板：支持网格和列表两种模式
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
        // 网格模式：2 列海报展示
        Grid() {
          ForEach(param.movies, (movie: Movie): void => {
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
              .onClick((): void => {
                this.goToDetail(movie.id);
              })
            }
          }, (movie: Movie): string => movie.id.toString())
        }
        .columnsTemplate('1fr 1fr')
        .columnsGap(12)
        .rowsGap(12)
        .width('100%')
        .padding(16)
      } else {
        // 列表模式：小海报 + 标题行
        List() {
          ForEach(param.movies, (movie: Movie): void => {
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
              .onClick((): void => {
                this.goToDetail(movie.id);
              })
            }
          }, (movie: Movie): string => movie.id.toString())
        }
        .width('100%')
      }
    }
  }
}
