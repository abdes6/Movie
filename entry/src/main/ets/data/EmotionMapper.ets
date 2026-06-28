// 情绪推荐映射器：10 种用户情绪 → TMDB 类型标签 + 评分阈值 + 文案
import { EmotionItem } from '../model/Models';
import { Constants } from '../common/Constants';

export class EmotionMapper {
  // 情绪定义列表，按顺序展示在首页
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
      // 随便看看：不指定类型，随机返回高分电影
      emoji: '🎬', label: '随便看看', genreIds: [],
      minRating: 0, recText: '随机推荐，给你一点小惊喜！'
    }
  ];

  // 根据情绪名称查找对应的 EmotionItem
  static getEmotionByLabel(label: string): EmotionItem | undefined {
    return EmotionMapper.EMOTIONS.find((e: EmotionItem): boolean => e.label === label);
  }
}
