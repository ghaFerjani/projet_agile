from boss import Boss
from filiale import Subsidiary
import unittest
from country import Country


class OuterTestClass(unittest.TestCase):
    print("start outer class")

    def setUp(self):
        self.country1 = Country()
        self.boss1 = Boss("Bernard Arnault", "LVMH")
        self.subsidiary1 = Subsidiary("LVMH", "Louis Vuitton", self.boss1, self.country1, self.country1)

    def testIsSubsidiary(self):
        self.assertEqual(self.subsidiary1.is_subsidiary(self.subsidiary1.pdg), True)


class InnerTestClass(unittest.TestCase):
    def setUp(self):
        self.country1 = Country()
        self.boss1 = Boss("Bernard Arnault", "LVMH")
        self.subsidiary1 = Subsidiary("LVMH", "Louis Vuitton", self.boss1, self.country1, self.country1)

    def testIsSubsidiary(self):
        self.assertEqual(self.subsidiary1.is_subsidiary(self.subsidiary1.pdg), True)


def test_inner_test_class(self):
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.InnerTestClass)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
