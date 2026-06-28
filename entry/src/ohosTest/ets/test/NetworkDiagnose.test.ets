import http from '@ohos.net.http';
import { describe, it, expect } from '@ohos/hypium';

const BAIDU_URL = 'https://www.baidu.com';

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
  });
}
