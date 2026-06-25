// 网络诊断测试：使用 @ohos.net.http（API 6 原生方式）验证网络连通性
import http from '@ohos.net.http';
import { describe, it, expect } from '@ohos/hypium';

const BAIDU_URL = 'https://www.baidu.com';
const TMDB_BASE_URL = 'https://api.themoviedb.org/3';
const TMDB_CONFIG_URL = `${TMDB_BASE_URL}/configuration?api_key=edb8215195923ea4410a96771ef5899d`;

function request(url: string): Promise<number> {
  return new Promise((resolve, reject) => {
    const req = http.createHttp();
    const timer = setTimeout(() => {
      req.destroy();
      reject(new Error('Operation timeout'));
    }, 10000);
    req.request(url, {
      method: http.RequestMethod.GET,
      connectTimeout: 5000,
      readTimeout: 8000
    }, (err: Error, resp: http.HttpResponse) => {
      clearTimeout(timer);
      req.destroy();
      if (err) {
        reject(err);
        return;
      }
      resolve(resp.responseCode);
    });
  });
}

export default function networkDiagnoseTest() {
  describe('NetworkDiagnoseTest', () => {
    it('testBaiduConnectivity', 0, async () => {
      const code = await request(BAIDU_URL);
      expect(code).assertEqual(200);
    });

    it('testTMDBConnectivity', 0, async () => {
      const code = await request(TMDB_CONFIG_URL);
      expect(code).assertEqual(200);
    });
  });
}
