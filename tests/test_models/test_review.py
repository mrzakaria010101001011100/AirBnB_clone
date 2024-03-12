import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_review_attributes(self):
        review = Review()

        # Test default values
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        # Test setting attributes
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This is a review."

        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "This is a review.")

if __name__ == '__main__':
    unittest.main()
