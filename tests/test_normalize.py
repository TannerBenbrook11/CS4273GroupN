from unittest.mock import mock_open, patch
from src.normalize import Normalizer
from src.utils import CSVReader
import unittest

class TestCSVFileReading(unittest.TestCase):
    def test_read_csv_file_success(self):
        """
        This unit test will check whether the content of the file was normalized correctly
        """
        # Mock CSV content
        csv_content = "identifier,machine_type,power_draw\n1,dell-5580,50\n2,dell-6580,20000\n3,dell-5580,30\n4,dell-6580,40000\n5,dell-7580,7500"
        
        # Use mock_open to simulate the file reading
        with patch("builtins.open", mock_open(read_data=csv_content)):
            csv_reader = CSVReader("dummy.csv")
            result = csv_reader.read_csv_file()

            # Normalize the content
            normalizer = Normalizer()
            result = normalizer.normalize_power_draw(result)
            
            # Verify the content is read correctly
            expected = [["identifier", "machine_type", "power_draw"], ["1", "dell-5580", "50"], ["2", "dell-6580", "20"], ["3", "dell-5580", "30"], ["4", "dell-6580", "40"], ["5", "dell-7580", "75"]]
            self.assertEqual(result, expected)