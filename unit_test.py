__author__ = 'student'

import unittest
from new_game import secret_number  # This is how you import a specific function to test from a file.


class MyTestCase(unittest.TestCase):
    def test_secret_number(self):  # Add the name of the function you are testing
        number = secret_number()  # add a
        self.assertIn(number, range(1, 101))  # This tests that the secret number is in the range.

# Add this function in the file you are testing.
if __name__ == '__main__':
    unittest.main()
