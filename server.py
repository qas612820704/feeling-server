from bottle import route, run, template

@route('/ping')
def ping():
    return 'pong'

run(host='0.0.0.0', port=8833)
