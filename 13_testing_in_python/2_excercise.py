'''
The idea of a unit test is that we're testing each piece of unit. These unit tests are small little pieces testing these simple functions.

'''

import unittest
import exercise_script


class TestGame(unittest.TestCase):
    try:
        def test_input(self):
            result = exercise_script.run_guess(5, 5)
            self.assertTrue(result)

        def test_input_wrong_guess(self):
            result = exercise_script.run_guess(5, 0)
            self.assertFalse(result)

        def test_input_wrong_number(self):
            result = exercise_script.run_guess(5, 11)
            self.assertFalse(result)

        def test_input_type(self):
            result = exercise_script.run_guess(5, '11')
            self.assertFalse(result)
    except Exception as err:
        print(err)


if __name__ == 'main':
    unittest.main()
