import tornado


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        para = self.get_argument('test', None)
        self.write("test tornado {}".format(para))
