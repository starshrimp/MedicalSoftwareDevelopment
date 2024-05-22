""" Data storage module"""

import json
import logging
import idgenerator


logging.basicConfig(filename='datastorage.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


class DataPoint(object):
    """ Data point class"""
    def __init__(self, patient_record_id, experiment_record_id, data):
        self.record_id = idgenerator.generate_unique_identifier()
        self.patient_record_id = patient_record_id
        self.experiment_record_id = experiment_record_id
        self.data = data

class DataStorage(object):
    """ Data storage class"""
    def __new__(cls):
        """ Singleton pattern"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataStorage, cls).__new__(cls)
            cls.instance.experiments = {}
            cls.instance.patients = {}
            cls.instance.data = []
        return cls.instance


    def create_patient(self, name):
        """ Create a new patient and return the record_id"""

        record_id = len(self.patients)
        self.patients[record_id] = name
        logger.info("Created patient with ID: %s, Name: %s", record_id, name)
        return record_id


    def create_experiment(self, name):
        """ Create a new experiment and return the record_id"""
        record_id = len(self.experiments)
        self.experiments[record_id] = name
        logger.info("Created experiment with ID: %s, Name: %s", record_id, name)
        return record_id


    def get_patients(self):
        """ Return all patients"""
        return self.patients


    def get_experiments(self):
        """ Return all experiments"""
        return self.experiments


    def add_data(self, dataobj):
        """ Add data to the data storage"""
        self.data.append(dataobj)
        logger.info("Added data: %s", dataobj)


    def store_data(self, filename):
        """ Store data into file"""
        self.store(filename, self.data)
        self.data.clear()
        logger.info("Stored data to %s.json", filename)


    def store_patients(self, filename):
        """ Store patients into file"""
        self.store(filename, self.patients)
        logger.info("Stored patient to %s.json", filename)


    def store_experiments(self, filename):
        """ Store experiments into file"""
        self.store(filename, self.experiments)
        logger.info("Stored experiment to %s.json", filename)


    def store(self, filename, data):
        """ Store data into file"""
        json_object = json.dumps(data, indent=4)
        with open(filename + ".json", "w") as outfile:
            outfile.write(json_object)
        logger.info("Stored %s items to %s.json", len(data), filename)
