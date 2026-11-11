import unittest
from features import reports

class TestReports(unittest.TestCase):
    def test_empty_history(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)

    def test_average_history(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)