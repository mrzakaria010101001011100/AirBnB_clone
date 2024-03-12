import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_state_attributes(self):
        state = State()

        # Test default values
        self.assertEqual(state.name, "")

        # Test setting attributes
        state.name = "California"

        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
