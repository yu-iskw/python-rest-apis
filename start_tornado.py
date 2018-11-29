import os

from tornado import ioloop, httpserver
from tornado.options import define, options

from rest.model.iris import IrisModel
from rest.tornado_app.app import make_app
from rest.utils import get_project_dir

if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')
    define('num_processes', default=0, help='number of processes')

    # Load model
    model_path = os.path.join(get_project_dir(), 'model', 'iris.joblib')
    model = IrisModel(model_path=model_path)

    # Single CPU
    # application = make_app(model=model, host=options.host)
    # server = application.listen(options.port)
    # ioloop.IOLoop.current().start()

    # Multiple CPUs
    # SEE: https://www.tornadoweb.org/en/stable/guide/running.html#processes-and-ports
    app = make_app(model=model, host=options.host)
    server = httpserver.HTTPServer(app)
    server.bind(options.port)
    # if num_proccesses is 0, forks one process per cpu
    server.start(options.num_processes)
    ioloop.IOLoop.current().start()
