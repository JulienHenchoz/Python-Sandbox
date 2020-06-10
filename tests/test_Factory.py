from unittest import TestCase
from models.Factory import Factory


class TestFactory(TestCase):
    def test_craft(self):
        factory = Factory(1, 2)
        factory.craft()
        self.assertEqual(0, factory.stock)

        factory.raw_materials = 3
        factory.craft()
        self.assertEqual(1, factory.stock)
        self.assertEqual(2, factory.raw_materials)

        factory.craft()
        self.assertEqual(2, factory.stock)
        self.assertEqual(1, factory.raw_materials)

        factory.craft()
        self.assertEqual(2, factory.stock)
        self.assertEqual(1, factory.raw_materials)

        factory.craft()
        self.assertEqual(2, factory.stock)
        self.assertEqual(1, factory.raw_materials)

    def test_set_stock_below_zero(self):
        factory = Factory(1, 2)
        factory.stock = -1
        self.assertEqual(0, factory.stock)

    def test_raw_materials_below_zero(self):
        factory = Factory(1, 2)
        factory.raw_materials = -1
        self.assertEqual(0, factory.raw_materials)