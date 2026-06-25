import { http } from '@kit.NetworkKit';
import { describe, beforeAll, beforeEach, afterEach, afterAll, it, expect } from '@ohos/hypium';
import { Constants } from '../../../main/ets/common/Constants';
import { MovieRepository } from '../../../main/ets/data/MovieRepository';
import { Movie, MovieDetail } from '../../../main/ets/model/Models';

const TMDB_CONFIG_URL = `${Constants.TMDB_BASE_URL}/configuration?api_key=${Constants.TMDB_API_KEY}`;
const TMDB_INVALID_KEY_URL = `${Constants.TMDB_BASE_URL}/configuration?api_key=INVALID_KEY_12345`;

function httpRequest(url: string): Promise<http.HttpResponse> {
  return new Promise((resolve, reject) => {
    const req = http.createHttp();
    req.request(url, {
      method: http.RequestMethod.GET,
      connectTimeout: 10000,
      readTimeout: 10000
    }, (err, resp) => {
      req.destroy();
      if (err) {
        reject(err);
        return;
      }
      resolve(resp);
    });
  });
}

export default function networkConnectivityTest() {
  describe('NetworkConnectivityTest', () => {
    it('testReachTMDB', 0, async () => {
      const resp = await httpRequest(TMDB_CONFIG_URL);
      expect(resp.responseCode).assertEqual(200);
    });

    it('testTMDBPopularResponse', 0, async () => {
      const repo = new MovieRepository();
      const movies: Movie[] = await repo.fetchPopular();
      expect(movies.length).assertLarger(0);
      expect(movies[0].title.length).assertLarger(0);
      expect(movies[0].posterPath).assertContain('https://');
      repo.destroy();
    });

    it('testInvalidApiKey', 0, async () => {
      let caught = false;
      try {
        await httpRequest(TMDB_INVALID_KEY_URL);
      } catch (e) {
        caught = true;
      }
      expect(caught).assertTrue();
    });

    it('testMovieDetailFields', 0, async () => {
      const repo = new MovieRepository();
      const knownMovieId = 550;
      const detail: MovieDetail = await repo.fetchMovieDetail(knownMovieId);
      expect(detail.title.length).assertLarger(0);
      expect(detail.runtime).assertLarger(0);
      expect(detail.director.length).assertLarger(0);
      expect(detail.cast.length).assertLarger(0);
      repo.destroy();
    });
  });
}
