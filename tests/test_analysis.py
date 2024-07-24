# tests/test_analysis.py
import unittest
from models.analysis import analyze_trends
import pandas as pd

class TestAnalysis(unittest.TestCase):
    def test_analyze_trends(self):
        data = pd.DataFrame({'close': [100, 105, 110, 115]})
        trends = analyze_trends(data)
        self.assertIn('price_change', trends.columns)

if __name__ == '__main__':
    unittest.main()

