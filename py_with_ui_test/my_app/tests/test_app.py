import unittest
from utils.db_helper import create_table, fetch_data

class TestApp(unittest.TestCase):
    def setUp(self):
        create_table()
    
    def test_fetch_data(self):
        data = fetch_data()
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
