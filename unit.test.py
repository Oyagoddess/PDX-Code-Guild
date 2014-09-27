__author__ = 'student'
# in pycharm, you can import the program you would like to test functions.
#by going into pycharm, opening a new file and choosing open with unittest  saving as test_filename)
# screen will have the functions that you need to update functions you want to test.
import unittest # this notates that it is in import unittest
import mock


from new_game import secret_number, user_name, make_guess
    # you want to import game by using from function and calling the file name
    # and you want to import the functions you want to call to test.


class MyTestCase(unittest.TestCase):
    def test_secret_number(self): # so you create input what you want to test this line is testing secret_number
        assert secret_number() in range(1, 100) # you want to assert or verify what it is testing and the results
        # wanting to test to make sure that the game secret number is between 1-100.
        # and you just run the program to see if function is doing what you wants.

# to test user inputs, you can download mock thru python by going into terminal through python and typing sudo pip install mock file.
    # this is the funciton to test with mock.patch
    def test_user_name(self):
        with mock.patch('__builtin__.raw_input', return_value = 'shalonda'):
	    assert user_name() == 'shalonda'
# follow same path of assert what is the outcome
    def test_make_guess(self):
# this test intergers.
        with mock.patch('__builtin__.int', return_value = '45'):
	    assert make_guess() == '45'

# however testing the mock.patch and random number takes a while to test and it ask
if __name__ == '__main__':
    unittest.main()
# calls and this runs the test.


