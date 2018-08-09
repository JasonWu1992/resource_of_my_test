import tornado.web
import os
from src.config import settings
from views.index import IndexHandler


class Applications(tornado.web.Application):
    def __init__(self):
        abs_path = os.path.dirname(os.path.abspath("__file__"))
        handlers = [
            (r'/GET', IndexHandler)
        ]
        static_path = os.path.join(abs_path, "static")
        super(Applications, self).__init__(handlers, static_path, **settings)
