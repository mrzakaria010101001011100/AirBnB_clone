import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_attributes(self):
        amenity = Amenity()

        # Test default values
        self.assertEqual(amenity.name, "")

        # Test setting attributes
        amenity.name = "Wi-Fi"

        self.assertEqual(amenity.name, "Wi-Fi")

if __name__ == '__main__':
    unittest.main()

