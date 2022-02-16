import unittest
from ems_optim import datasets

class SqlDbTestCase(unittest.TestCase):
    def setUp(self):
        """Test __init__
        """
        self.sqldb = datasets.SqlDb()
    def test_connect(self):
        """Test connect
        """
        self.assertEqual(0,0)
    def test_weather(self):
        """Test weather
        """
        self.assertEqual(0,0)

if __name__ == '__main__':
    unittest.main()