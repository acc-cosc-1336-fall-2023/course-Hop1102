#
import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_die_rolls(self):
        die = Die()

        for _ in range(3):
            die.roll()
            rolled_value = die.get_rolled_value()

            self.assertTrue(1 <= rolled_value <= 6, f"invalid die roll: {rolled_value}")

    def test_die_str_method(self):
        die = Die()
        die.roll()
        expected_str = f"The rolled value is {die.get_rolled_value()}"
        self.assertEqual(str(die), expected_str, "Invalid __str__ method")

