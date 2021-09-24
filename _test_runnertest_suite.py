import unittest
from main import *

# Add imports here!
import os
import requests

class UnitTests(unittest.TestCase):

  def test_Bot(self):
      # Enter code here
      response = requests.get(os.environ.get("url"))
      self.assertEqual(response.status_code,200)

