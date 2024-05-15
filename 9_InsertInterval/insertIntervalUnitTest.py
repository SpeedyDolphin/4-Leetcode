from intertInterval import insert
import unittest

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_midInsertMerge(self):         
        self.assertEqual(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]) 

    def test_midInsert(self):
        self.assertEqual(insert([[1,5]], [2,7]), [[1,7]])

    def test_insertStartMerge(self):
        self.assertEqual(insert([[1,5]], [0,3]), [[0,5]])

if __name__ == '__main__': 
    unittest.main() 