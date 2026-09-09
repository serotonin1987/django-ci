from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Product


class ProductTestCase(TestCase):

    def check_product(self, product):
        self.assertEqual(product.name, "iPhone")
        self.assertEqual(product.price, 500000)
        self.assertEqual(product.quantity, 10)

    def test_product_creation(self):
        product = Product.objects.create(name="iPhone", price=500000, quantity=10)
        self.check_product(product)

    def test_negative_price(self):
        product = Product(name="iPhone", price=-100, quantity=10)
        with self.assertRaises(ValidationError):
            product.full_clean()