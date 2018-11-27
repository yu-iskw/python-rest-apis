#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import tornado.ioloop
from tornado import web
from tornado.options import define, options


class IrisPredictHandler(web.RequestHandler):
    # SUPPORTED_METHODS = ("POST")

    def post(self):
        response = {
            'message': "hello"
        }
        self.set_status(200)
        self.write(response)


def make_app(host='localhost'):
    return tornado.web.Application([
        (r"/", IrisPredictHandler),
    ], default_host=host)


if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')

    application = make_app(host=options.host)
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
