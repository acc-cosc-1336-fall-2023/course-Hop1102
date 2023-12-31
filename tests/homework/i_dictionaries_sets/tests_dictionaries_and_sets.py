#
#import unittest
#from src.homework.i_dictionaries_sets.dictionary import get_p_distance
#from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix

#class Test_Config(unittest.TestCase):

    #def test_get_p_distance(self):
       # result = get_p_distance(
         #   ['T','T','T','C','C','A','T','T','T','A'],
          #  ['G','A','T','T','C','A','T','T','T','C']
       # )
       # self.assertAlmostEqual(result, 0.4, places=5)

   #def test_get_p_distance_matrix(self):
      #  strings = [
       #     ['T','T','T','C','C','A','T','T','T','A'],
       #     ['G','A','T','T','C','A','T','T','T','C'],
       #     ['T','T','T','C','C','A','T','T','T','T'],
       #     ['G','T','T','C','C','A','T','T','T','A']
      #  ]
       #  expected_outcome = [
      #      [0.0, 0.4, 0.1, 0.1],
      #      [0.4, 0.0, 0.4, 0.3],
      #      [0.1, 0.4, 0.0, 0.2],
      #      [0.1, 0.3, 0.2, 0.0]
      #  ]
       # result = get_p_distance_matrix(strings) 
      #  self.assertEqual(result, expected_outcome)

#import unittest
#from src.homework.i_dictionaries_sets.dictionary import add_inventory
#from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

#class Test_Config(unittest.TestCase):
   
 #   def test_add_inventory(self):
 #       inventory_dictionary = {}
 #       add_inventory(inventory_dictionary, 'Widget1', 10)
  #      self.assertEqual(inventory_dictionary['Widget1'], 10) 
#
 #       add_inventory(inventory_dictionary, 'Widget1', 25)
 #       self.assertEqual(inventory_dictionary['Widget1'], 35)
        
 #       add_inventory(inventory_dictionary, 'Widget1', -10)
 #       self.assertEqual(inventory_dictionary['Widget1'], 25) 

 #   def test_remove_inventory_widget(self):
  #      inventory_dictionary = {} 
  #      add_inventory(inventory_dictionary, 'Widget1', 10)
  #      add_inventory(inventory_dictionary, 'Widget2', 5)

  #      result = remove_inventory_widget(inventory_dictionary, 'Widget1')

    #    self.assertEqual(len(inventory_dictionary), 1)
   #     self.assertIn('Widget2', inventory_dictionary)
   #     self.assertEqual(result, 'record deleted') 


import unittest

class Test_Config(unittest.TestCase):
    def set_list(self):
        self.baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        self.basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

    def test_intersection(self):
        result = self.baseball.intersection(self.basketball)
        expected = {'Carmen', 'Alicia'}
        self.assertEqual(result, expected)

    def test_union(self):
        result = self.baseball.union(self.basketball)
        expected = {'Eva', 'Carmen', 'Alicia', 'Jodi', 'Sarah', 'Aida'}
        self.assertEqual(result, expected)

    def test_diff_baseball(self):
        result = self.baseball.difference(self.basketball)
        expected = {'Jodi', 'Aida'}
        self.assertEqual(result, expected)

    def test_diff_basketball(self):
        result = self.basketball.difference(self.baseball)
        expected = {'Eva', 'Sarah'}
        self.assertEqual(result, expected)

    def test_symmetric_difference(self):
        result = self.baseball.symmetric_difference(self.basketball)
        expected = {'Eva', 'Jodi', 'Sarah', 'Aida'}
        self.assertEqual(result, expected)


