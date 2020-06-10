from unittest import TestCase
from models.Farm import Farm


class TestFarm(TestCase):
    def test_craft(self):
        farm = Farm(1, 2)
        farm.craft()
        self.assertEqual(1, farm.stock)

        farm.craft()
        self.assertEqual(2, farm.stock)

        farm.craft()
        self.assertEqual(2, farm.stock)

    def test_set_stock_below_zero(self):
        farm = Farm(1, 2)
        farm.stock = -1
        self.assertEqual(0, farm.stock)
