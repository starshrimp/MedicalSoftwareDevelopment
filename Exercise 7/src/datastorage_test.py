""" Test the DataStorage class """

import unittest
from unittest.mock import patch, mock_open
import json
import datastorage

class TestDataStorage(unittest.TestCase):
    """ Test the DataStorage class """

    def setUp(self):
        """ Set up test environment """
        self.data_storage = datastorage.DataStorage()
    
    def test_create_patient(self):
        """ Test the create_patient method """
        data_storage = datastorage.DataStorage()
        result = data_storage.create_patient("David Herzig")
        self.assertTrue(result >= 0)

    @patch('builtins.open', new_callable=mock_open) # mock is used to simulate the open function
    def test_store_patients(self, mock_file):
        """ Test the store_patients method """
        self.data_storage.create_patient("Patient 1")
        self.data_storage.create_patient("Patient 2")
        self.data_storage.store_patients("patients_test")

        # Check if the file was opened correctly
        mock_file.assert_called_with("patients_test.json", "w")

        # Check the content written to the file
        handle = mock_file()
        written_content = handle.write.call_args[0][0]
        expected_content = json.dumps(self.data_storage.get_patients(), indent=4)
        self.assertEqual(written_content, expected_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_store_experiments(self, mock_file):
        """ Test the store_experiments method """
        self.data_storage.create_experiment("Experiment 1")
        self.data_storage.create_experiment("Experiment 2")
        self.data_storage.store_experiments("experiments_test")

        # Check if the file was opened correctly
        mock_file.assert_called_with("experiments_test.json", "w")

        # Check the content written to the file
        handle = mock_file()
        written_content = handle.write.call_args[0][0]
        expected_content = json.dumps(self.data_storage.get_experiments(), indent=4)
        self.assertEqual(written_content, expected_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_store_data(self, mock_file):
        """ Test the store_data method """
        data_point = datastorage.DataPoint(1, 1, "Sample data")
        self.data_storage.add_data(data_point)
        self.data_storage.store_data("data_test")

        # Check if the file was opened correctly
        mock_file.assert_called_with("data_test.json", "w")

        # Check the content written to the file
        handle = mock_file()
        written_content = handle.write.call_args[0][0]
        expected_content = json.dumps(self.data_storage.data, indent=4)
        self.assertEqual(written_content, expected_content)


if __name__ == '__main__':
    unittest.main()
