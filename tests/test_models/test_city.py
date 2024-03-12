import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_city_attributes(self):
        city = City()

        # Test default values
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        # Test setting attributes
        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()

