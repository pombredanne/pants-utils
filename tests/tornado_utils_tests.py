import tornado.web
import tornado.testing

from pants_utils import tornado_utils

class PantsUtilsTornadoTestCase(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return tornado.web.Application(
            [
                (r'/static/(.*)', tornado_utils.PexStaticFileHandler,
                 dict(path='tests', subdir='static'))
            ])

    def test_get_staticfile_200(self):
        self.http_client.fetch(self.get_url('/static/staticfile.txt'), self.stop)
        response = self.wait()
        self.assertEqual(response.code, 200)

    def test_get_staticfile_404(self):
        self.http_client.fetch(self.get_url('/static/i/dont/exist.txt'), self.stop)
        response = self.wait()
        self.assertEqual(response.code, 404)
