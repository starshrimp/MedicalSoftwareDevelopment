import idgenerator

class DataPoint(object):
  def __init__(self, patient_id, experiment_id, data):
    self.id = idgenerator.create_unique_identifier()
    self.patient_id = patient_id
    self.experiment_id = experiment_id
    self.data = data

class DataStorage(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(DataStorage, cls).__new__(cls)
      cls.instance.experiments = {}
      cls.instance.patients = {}
      cls.instance.data = {}
    return cls.instance
    
  def create_patient(self, name):
    id = len(self.patients)
    self.patients[id] = name
    return id
    
  def create_experiment(self, name):
    id = len(self.experiments)
    self.experiments[id] = name
    return id
    
  def get_patients(self):
    return self.patients
    
  def get_experiments(self):
    return self.experiments
    
  def add_data(self, patient_id, experiment_id, data):
    dObj = Data(patient_id, experiment_id, data)
    self.data.append(dObj)

  def store_data(self, filename):
    # store data into file
    self.data.clear()