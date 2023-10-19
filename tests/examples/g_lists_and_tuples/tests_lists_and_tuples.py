import unittest

from src.examples.g_lists_and_tuples.lists import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_list_slicing_start_end(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 

        self.assertEqual(days[2:5], ['Tuesday', 'Wednesday', 'Thursday'])

    def test_list_slicing_start_no_end(self):
        list = [1,2,3,4,5]

        self.assertEqual(list[2:], [3,4,5])

    def test_list_slicing_w_step(self):
        list = [1,2,3,4,5,6,7,8,9,10]

        self.assertEqual(list[1:8:2], [2,4,6,8])

    def test_list_slicing_start_from_end(self):
        list = [1,2,3,4,5,6,7,8,9,10]

        self.assertEqual(list[-5:], [6,7,8,9,10])
        