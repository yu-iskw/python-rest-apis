from tornado import ioloop
from tornado.options import define, options

from rest.tornado_app.app import make_app


if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')
    define('restart_interval', default=2, help='interval seconds to restart server.')

    application = make_app(host=options.host)
    server = application.listen(options.port)
    ioloop.IOLoop.current().start()
