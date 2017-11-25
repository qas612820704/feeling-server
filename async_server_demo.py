from bottle import Bottle
from paste import httpserver
import time

app = Bottle()

if __name__ == '__main__':
    flag = False

    @app.route('/')
    def foo():
        global flag
        while not flag is True:
            pass
        return 'hello, world!\n'

    @app.route('/delay')
    def foo():
        global flag
        flag = True
        return 'trigger\n'

app.run(server='paste', host='0.0.0.0', port=8080)
# httpserver.serve(app, host='0.0.0.0', port=8080)
