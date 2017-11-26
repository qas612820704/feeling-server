from bottle import Bottle, post, request, response
from urllib import parse
import json
import os

app = Bottle()

state = {
    'directionData': {},
    'colorQuestData': {}
}

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/ping')
def ping():
    return 'pong'

@app.post('/api_v1/update/orientation/')
def updateOrientation():
    data = request.body.read().decode('utf-8')
    j_data = json.loads(data)
    state['orientation']['absolute'] = j_data['absolute']
    state['orientation']['alpha'] = j_data['alpha']
    state['orientation']['beta'] = j_data['beta']
    state['orientation']['gamma'] = j_data['gamma']
    return {
        'status': 'sccuess'
    }

@app.post('/api_v2/update/direction/')
def update():
    global state
    try:
        data = parse.unquote(request.body.read().decode('utf-8'))
        state['directionData'] = json.loads(data)
    except:
        return { 'status': 'fail' }
    return { 'status': 'sccuess' }

@app.post('/api_v2/update/color_quest/')
def updateColorQuest():
    global state
    try:
        data = parse.unquote(request.body.read().decode('utf-8'))
        state['colorQuestData'] = json.loads(data)
    except:
        print ('updateColorQuest', 'fail')
        return { 'status': 'fail' }
    return { 'status': 'sccuess'}

@app.get('/data/')
def getData():
    return state

@app.get('/api_v2/init_data/')
def getInitData():
    return state

@app.get('/api_v2/data/')
def getDataV2():
    global state
    prevState = state.copy()
    while prevState == state:
        pass
    return state

if 'PROD' in os.environ:
    app.run(server='paste', host='0.0.0.0', port=8833)
else:
    app.run(host='0.0.0.0', port=8833)
