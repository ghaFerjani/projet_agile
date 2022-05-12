from boss import Boss
from filiale import Subsidiary
from town import Town
from country import Country
import unittest


class SubsidiaryTest(unittest.TestCase):
    def setUp(self):
        self.country1 = Country()
        self.boss1 = Boss("Bernard Arnault", "LVMH")
        self.subsidiary1 = Subsidiary("LVMH", "Louis Vuitton", self.boss1, self.country1, self.country1)

    def testIsSubsidiary(self):
        self.assertEqual(self.subsidiary1.is_subsidiary(self.boss1), True)

class TownTestCase(unittest.TestCase):
    def test_gdp_town(self):
        country1 = Country()
        town = Town(country1)
        result = town.gdp_town()
        self.assertEqual(76000000, result)


class CountryTestCase(unittest.TestCase):
    def test_gdp_country(self):
        country1 = Country()
        town_1 = Town(country1, "Paris", 38, 2_000_000)
        town_2 = Town(country1, "Lyon", 25, 500_000)
        country1.add_towns([town_1, town_2])
        result = country1.gdp_country()
        self.assertEqual(88500000, result)


if __name__ == '__main__':
    unittest.main()
