import sys
sys.path.append('backend/test')
from AuthTest import TestApp
from DeckTest import TestApp
import unittest

if __name__=="__main__":
  #AuthTest.TestApp(unittest.TestCase)
  #DeckTest.TestApp(unittest.TestCase)
  unittest.main()
