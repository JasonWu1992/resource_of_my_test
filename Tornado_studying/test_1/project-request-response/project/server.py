import tornado.web
import tornado.ioloop
import os
import tornado.httpserver
from src.config import options
from src.appliction import Applications
# from


if __name__ == '__main__':
    app = Applications()
    # 监听端口
    # 实例化服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options["port"])
    tornado.ioloop.IOLoop.current().start()
