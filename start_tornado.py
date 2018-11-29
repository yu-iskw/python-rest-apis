from tornado import ioloop, httpserver
from tornado.options import define, options

from rest.tornado_app.app import make_app


if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')
    define('num_processes', default=0, 'number of processes')

    # Single CPU
    # application = make_app(host=options.host)
    # server = application.listen(options.port)
    # ioloop.IOLoop.current().start()

    # Multiple CPUs
    # SEE: https://www.tornadoweb.org/en/stable/guide/running.html#processes-and-ports
    app = make_app(host=options.host)
    server = httpserver.HTTPServer(app)
    server.bind(options.port)
    # if num_proccesses is 0, forks one process per cpu
    server.start(options.num_processes)
    ioloop.IOLoop.current().start()
