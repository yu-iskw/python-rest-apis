import datetime
from tornado import ioloop
from tornado.options import define, options

from rest.tornado_app.app import make_app


def stop_tornado():
    """Stop ioloop."""
    current_ioloop = ioloop.IOLoop.current()
    current_ioloop.add_callback(current_ioloop.stop)
    print("ioloop is stopped.")


if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')
    define('restart_interval', default=30, help='interval seconds to restart server.')

    application = make_app(host=options.host)
    server = application.listen(options.port)

    # Restart to defence against memory leak.
    while True:
        ioloop.IOLoop.current().add_timeout(
            datetime.timedelta(seconds=options.restart_interval),
            stop_tornado)
        ioloop.IOLoop.current().start()
        print("ioloop is started.")
        # server.stop()
