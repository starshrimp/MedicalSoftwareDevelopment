import unittest
from unittest.mock import MagicMock, patch
from file_upload import process_fasta_from_file
from logging_config import setup_logging

setup_logging()
class TestProcessFasta(unittest.TestCase):

    @patch('file_upload.handle_errors')
    def test_error_handling(self, mock_handle_errors):

        broken_file = MagicMock()
        broken_file.getvalue.side_effect = Exception("Simulated file reading exception")

        # Execute the function with the problematic file
        result = process_fasta_from_file(broken_file)

        # Check if handle_errors was called due to the exception
        mock_handle_errors.assert_called()

        # Optionally, check if the result is as expected (likely an empty list)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
