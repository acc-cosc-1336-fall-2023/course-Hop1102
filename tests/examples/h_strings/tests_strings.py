
from typing import Self
import unittest

from src.examples.h_strings.strings import concat_strings, search_in_string, slice_string, slice_w_step_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_configuration(self):
        self.assertEqual(True, test_config())


    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc", "def"), "abcdef")
    
    def test_slice_string(self):
        name = "patty lynn Smith"
        self.assertEqual(slice_string(name), "lynn")
        self.assertEqual(name[11:],"Smith")

    #def test_slice_w_step_value(self):
        #letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #self.assertEqual(slice_w_step_value(letters), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_search_in_strings(self):
        str1 = 'abc'
        str2 = 'abcdef'

        self.assertEqual(search_in_string(str1, str2), True)
        self.assertEqual(search_in_string('efg', str2), False)

    def test_compare_strings(self):
        str1 = 'c'
        str2 = 'p' 

        self.assertEqual(str1 < str2, True) 
        self.assertEqual(str2 < str1, False) 
        self.assertEqual('c++' == 'C++', False) 

    def test_is_string_digit(self):
        str1 = '1200'
        self.assertEqual(str1.isdigit(), True)
        self.assertEqual("ab".isdigit(), False)

    def test_string_is_alpha(self):
        str1 = 'abcdefg'
        self.assertEqual(str1.isalpha(), True)
        self.assertEqual('$%1'.isalpha(), False)
                     
    def test_string_is_alpha(self):
        str1 = "XYZ"
        self.assertEqual(str1.isupper(), True)

    def test_string_to_lower(self):
        str1 = "aBcDeF"
        self.assertEqual(str1.lower(), "abcdef")

    def test_string_to_upper(self):
        str1 = "aBcDeF"
        self.assertEqual(str1.upper(), "ABCDEF")

    #def test_string_char_from_strings(self):
        #str1 = "eeabcdefgefe"
        #self.assertEqual(str1.strip("e"), "abcdefgefe")

    def test_lstrip_char_from_strings(self):
        str1 = "aaaaxyz"
        self.assertEqual(str1.lstrip("a"), "xyz")

    def test_rstrip_char_from_strings(self):
        str1 = "abcyyy"
        self.assertEqual(str1.rstrip("y"), "abc")

    def test_replace_from_string(self):
        str1 = "eeabcdefgefe"
        self.assertEqual(str1.replace("e", ""), "abcdfgf")

    def test_string_repetition_operator(self):
        str1 = 'w' * 5 
        self.assertEqual(str1, "wwwww")

    def test_split_string(self):
        str1 = "one/ttwo/tthree/tfour"
        str_list = str1.split("/t")
        self.assertEqual(str)
