__author__ = 'student'

import unittest
from new_game import secret_number


class MyTestCase(unittest.TestCase):
    def test_secret_number(self):
        number = secret_number()
        self.assertIn(number, range(1, 101))



if __name__ == '__main__':
    unittest.main()
