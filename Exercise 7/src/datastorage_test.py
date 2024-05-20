""" Test the DataStorage class """

import unittest
import datastorage

class TestDataStorage(unittest.TestCase):
    """ Test the DataStorage class """
    def test_create_patient(self):
        """ Test the create_patient method """
        data_storage = datastorage.DataStorage()
        result = data_storage.create_patient("David Herzig")
        self.assertTrue(result >= 0)

if __name__ == '__main__':
    unittest.main()
