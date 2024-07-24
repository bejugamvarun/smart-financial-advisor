# tests/test_recommendation.py
import unittest
from models.recommendation import generate_recommendation
import pandas as pd

class TestRecommendation(unittest.TestCase):
    def test_generate_recommendation(self):
        data = pd.DataFrame({'close': [100, 105, 110, 115]})
        recommendation = generate_recommendation(data)
        self.assertIn("The stock is performing well", recommendation)

if __name__ == '__main__':
    unittest.main()
