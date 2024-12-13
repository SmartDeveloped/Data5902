import unittest
from smallest_num  import smallest
#new edit
class testFunc(unittest.TestCase):

    def test_positve(self):
       result = smallest(3, 8)
       self.assertEqual(result, 3)

    def test_negative(self):
        result = smallest(-34, -17)
        self.assertEqual(result, -34)

    
if __name__ == '__main__':
    unittest.main()