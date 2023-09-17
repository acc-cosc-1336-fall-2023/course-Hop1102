import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_number, multiply_number

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        #test that the function get_number returns 1
        self.assertEqual(1, get_number(1))
    
    def test_get_number_2(self):
        #test that the function get_number returns 2
        self.assertEqual(2, get_number(2))
         def test_configuration(self):
        self.asstEqual(True, test_config())
        
    def test_and_truth_tables(self):
        self.assertEqual(True, get_and_result(True, True))
        self.assertEqual(False, get_and_result(True, False))
        self.assertEqual(False, get_and_result(True, True))
        self.assertEqual(False, get_and_result(True, True))

    def test_or_truth_tables(self):
        self.assertEqual(True, get_or_result(True, True))
        self.assertEqual(True, get_or_result(True, False))
        self.assertEqual(True, get_or_result(False, True))
        self.assertEqual(False,get_or_result(False, False))

    def test_not_truth_tables(self):
        self.assertEqual(True, get_not_value(False))
        self.assertEqual(True, get_not_value(True))

    def test_is_even(self):
        self.assertEqual(False, is_even(1))
        self.assertEqual(True, is_even(2))
        self.assertEqual(False, is_even)

    def test_is_vowel(self): 
        self.assertEqual(True, is_vowel('a')) 
        self.assertEqual(False, is_vowel('e'))
        self.assertEqual(False, is_vowel('i'))
        self.assertEqual(False, is_vowel('o'))
        self.assertEqual(False, is_vowel('u'))

    def test_is_consonant(self):
        self.assertEqual(False, is_consonant('a'))
        self.assertEqual(True, is_consonant('b'))


    

    def test_get_multiply_numbers(self):
        self.assertEqual(25, multiply_number(5, 5)) 
        self.assertEqual(100, multiply_number(10, 10))

