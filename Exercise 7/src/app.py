""" Main application file for the data collection service exercise"""
# import os
# import tracemalloc
# import psutil


import json
import logging
from flask import request, Flask
import datastorage


app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

class Experiment:
    """Experiment class"""
    def __init__(self, record_id, name):
        self.record_id = record_id
        self.name = name


def to_json(obj):
    """Convert object to json format"""
    return json.dumps(obj, default=lambda obj: obj.__dict__)

@app.route('/info', methods=['GET'])
def index():
    """Return information about the application"""
    logger.info("Accessed the info endpoint")
    return json.dumps({'application' : 'Data Collection Service',
    'author' : 'Davrecord_id Herzig', 'version' : 'v1_0_1', 
    'Support' : 'dave.herzig@gmail.com', 'adjusted by' : 'Sarah Rebecca Meyer', 
    'logging' : 'app.log'})

@app.route('/experiment', methods=['POST', 'GET'])

def experiment_action():
    """Create a new experiment or get all experiments"""

    data_storage = datastorage.DataStorage()
    if request.method == 'POST':
        form_data = request.data
        data = json.loads(form_data)
        record_id = data_storage.create_experiment(data['name'])
        logger.info("POST: Created experiment with ID: %s", record_id)
        return json.dumps({'result' : record_id})
    if request.method == 'GET':
        exps = data_storage.get_experiments()
        exps_array = []
        for key, value in exps.items():
            exp = Experiment(key, value)
            exps_array.append(exp)
        logger.info("GET: Retrieved all experiments")
        return to_json(exps_array)

@app.route('/patient', methods=['POST', 'GET'])
def patient_action():
    """Create a new patient or get all patients"""
    data_storage = datastorage.DataStorage()
    if request.method == 'POST':
        form_data = request.data
        data = json.loads(form_data)
        record_id = data_storage.create_patient(data['name'])
        logger.info("POST: Created patient with ID: %s", record_id)
        return json.dumps({'result' : record_id})
    if request.method == 'GET':
        logger.info("GET: Retrieved all patients")
        return data_storage.get_patients()


@app.route('/store', methods=['POST'])
def store_data():
    """Store data in the data storage"""
    data_storage = datastorage.DataStorage()
    form_data = request.data
    data = json.loads(form_data)
    filename = data['filename']
    data_type = data['type']


    if data_type == 'experiments':
        data_storage.store_experiments(filename)
    elif data_type == 'patients':
        data_storage.store_patients(filename)
    elif data_type == 'data':
        data_storage.store_data(filename)
    else:
        logger.error("Invalid data type: %s", data_type)

    logger.info("Stored %s data to %s.json", data_type, filename)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/data', methods=['POST'])
def upload_data():
    """Upload data to the data storage"""
    form_data = request.data
    print(form_data)
    data = json.loads(form_data)
    data_storage = datastorage.DataStorage()
    data_storage.add_data(data)
    logger.info("Data uploaded: %s", data)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=8080)
    #app.run(debug=True, port=8080)
