# tests/test_data_processor.py
import unittest

from data.data_processor import process_stock_data_alpha_vantage


class TestDataProcessor(unittest.TestCase):
    def test_process_stock_data_alpha_vantage(self):
        raw_data = {
            "2023-01-01 09:30:00": {"1. open": "150.0", "2. high": "151.0", "3. low": "149.0", "4. close": "150.5",
                                    "5. volume": "10000"}
        }
        data = process_stock_data_alpha_vantage(raw_data)
        self.assertEqual(len(data), 1)


if __name__ == '__main__':
    unittest.main()
