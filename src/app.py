import datastorage

import json
from flask import request, Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return json.dumps({'name' : 'David',
    'mail' : 'david.herzig@roche.com'})

@app.route('/experiment', methods=['POST', 'GET'])
def create_experiment():
  ds = datastorage.DataStorage()
  if request.method == 'POST':
    form_data = request.data
    data = json.loads(form_data)
    id = ds.create_experiment(data['name'])
    return json.dumps({'result' : id})
  elif request.method == 'GET':
    return ds.get_experiments()
  
@app.route('/patient', methods=['POST', 'GET'])
def create_patient():
  ds = datastorage.DataStorage()
  if request.method == 'POST':
    name = request.args.get('name')
    ds = datastorage.DataStorage()
    id = ds.create_patient(name)
    return json.dumps({'result' : id})
  elif request.method == 'GET':
    return ds.get_patients()
  
@app.route('/store', methods=['POST'])
def store_data():
  pass
  
@app.route('/upload', methods=['POST'])
def upload_data(data):
  pass
  

if __name__ == '__main__':
  print('Hello World')
  
  ds = datastorage.DataStorage()
  print(ds.create_experiment('Experiment'))
  print(ds.get_experiments())
  
  ds2 = datastorage.DataStorage()
  print(ds2.create_experiment('Experiment2'))
  print(ds2.get_experiments())
  

