import { HomeContent } from '../view/HomeContent';
import { DiscoverContent } from '../view/DiscoverContent';
import { MineContent } from '../view/MineContent';

interface TabBuilderParam {
  icon: string;
  text: string;
  index: number;
}

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

  @Builder TabBuilder(param: TabBuilderParam) {
    Column() {
      Text(param.icon)
        .fontSize(20)
        .fontColor(this.currentIndex === param.index ? '#1890ff' : '#999')
      Text(param.text)
        .fontSize(10)
        .margin({ top: 2 })
        .fontColor(this.currentIndex === param.index ? '#1890ff' : '#999')
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
