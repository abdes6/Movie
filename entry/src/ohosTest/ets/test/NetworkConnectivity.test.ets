import { describe, it, expect } from '@ohos/hypium';
import { MovieRepository } from '../../../main/ets/data/MovieRepository';
import { Movie, MovieDetail } from '../../../main/ets/model/Models';

export default function networkConnectivityTest() {
  describe('NetworkConnectivityTest', () => {
    it('testFlaskPopularResponse', 0, async () => {
      const repo = new MovieRepository();
      const movies: Movie[] = await repo.fetchPopular();
      expect(movies.length).assertLarger(0);
      expect(movies[0].title.length).assertLarger(0);
      expect(movies[0].posterPath).assertContain('5000');
      repo.destroy();
    });

    it('testMovieDetailFields', 0, async () => {
      const repo = new MovieRepository();
      const knownMovieId = 1;
      const detail: MovieDetail = await repo.fetchMovieDetail(knownMovieId);
      expect(detail.title.length).assertLarger(0);
      expect(detail.runtime).assertLarger(0);
      expect(detail.director.length).assertLarger(0);
      expect(detail.cast.length).assertLarger(0);
      repo.destroy();
    });
  });
}
