import sys
sys.path.append('backend/test')
from AuthTest import AuthTestApp
from DeckTest import DeckTestApp
from CardTest import CardTestApp
import unittest

if __name__=="__main__":
  #AuthTest.TestApp(unittest.TestCase)
  #DeckTest.TestApp(unittest.TestCase)
  unittest.main()
