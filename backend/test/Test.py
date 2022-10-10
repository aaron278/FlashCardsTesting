import sys
sys.path.append(backend/test)
import AuthTest
#import DeckTest
import unittest

if __name__=="__main__":
  AuthTest.TestApp(unittest.TestCase)
  #DeckTest.TestApp(unittest.TestCase)
  unittest.main()
