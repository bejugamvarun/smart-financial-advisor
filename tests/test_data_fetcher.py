# tests/test_data_fetcher.py
import unittest

from data.data_fetcher import fetch_stock_data_alpha_vantage


class TestDataFetcher(unittest.TestCase):
    def test_fetch_stock_data_alpha_vantage(self):
        data = fetch_stock_data_alpha_vantage("AAPL")
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
