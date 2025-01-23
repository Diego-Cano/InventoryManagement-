import unittest
from inventory import duplicate_zeros

class TestDuplicateZeros(unittest.TestCase):
    def test_normal_case(self):
        inventory = [4, 0, 1, 3, 0, 2, 5, 0]
        duplicate_zeros(inventory)
        self.assertEqual(inventory, [4, 0, 0, 1, 3, 0, 0, 2])
        
    def test_normal_case_2(self):
        inventory = [1, 2, 3, 0, 4]
        duplicate_zeros(inventory)
        self.assertEqual(inventory, [1, 2, 3, 0, 0])

    def test_normal_case_3(self):
        inventory = [0, 0, 0]
        duplicate_zeros(inventory)
        self.assertEqual(inventory, [0, 0, 0])
