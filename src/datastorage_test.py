import unittest

import datastorage

class TestDataStorage(unittest.TestCase):

    def test_create_patient(self):
        ds = datastorage.DataStorage()
        result = ds.create_patient("David Herzig")
        self.assertTrue(result >= 0)

if __name__ == '__main__':
    unittest.main()