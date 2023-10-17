#
from os import name
import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        dna1 = "GAGCCTACTAACGGGAT" 
        dna2 = "CATCGTAATGACGGCCT"
        expected_result = 7
        result = get_hamming_distance(dna1, dna2)
        assert result == expected_result 

    def test_get_dna_complement(self):
        dna = "AAAACCCGGT"
        expected_result = "ACCGGGTTTT"
        result = get_dna_complement(dna)
        assert result == expected_result 