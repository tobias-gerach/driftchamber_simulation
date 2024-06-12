
import unittest

from datastore import DataStore
from modules.Chamber import Chamber

class ChamberTest(unittest.TestCase):
    """
    Test class for the Chamber class
    """

    def test_chamber_is_in_datastore(self):
        ds = DataStore()
        superlayerlist = [1, 2, 1]
        width = 5
        field = ["ooooo", "OOOOO", "OOOOO", "ooooo"]
        Chamber(superlayerlist, width, ds)
        
        chamber = ds.get('chamber')
        self.assertEqual(chamber.getHight(), 4)
        self.assertEqual(chamber.getWidth(), 5)
        self.assertEqual(chamber.getField(), field)
