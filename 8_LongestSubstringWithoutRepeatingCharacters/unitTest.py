from LongestSubstringWithoutRepeatingCharacters import *
import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_abcabcbb(self):         
        self.assertEqual(attempt2('abcabcbb'), 3) 

    def test_au(self):         
        self.assertEqual(attempt2('au'), 2) 

    def test_dvdf(self):         
        self.assertEqual(attempt2('dvdf'), 3) 

    def test_asjrgapa(self):         
        self.assertEqual(attempt2('asjrgapa'), 6) 

    def test_pwwkew(self):         
        self.assertEqual(attempt2('pwwkew'), 3) 

    def test_bbbbbbbbbbbbbb(self):         
        self.assertEqual(attempt2('bbbbbbbbbbbbbb'), 1) 

    def test_loddktdji(self):         
        self.assertEqual(attempt2('loddktdji'), 5) 
  
if __name__ == '__main__': 
    unittest.main() 