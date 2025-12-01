import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from product.factories import ProductFactory, CategoryFactory
from product.models import Product


class TestProductViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = ProductFactory()  # This will create with a category

    def test_get_all_product(self):
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = response.json()

        # Adjust based on your actual API response structure
        if 'results' in product_data:
            product_data = product_data['results']

        self.assertEqual(product_data[0]["title"], self.product.title)
        self.assertEqual(product_data[0]["price"], self.product.price)
        # Note: field is called 'activate' not 'active'
        self.assertEqual(product_data[0]["activate"], self.product.activate)

    def test_create_products(self):
        category = CategoryFactory()
        data = {
            "title": "notebook",
            "description": "A great notebook",
            "price": 800,  # Integer for PositiveBigIntegerField
            "activate": True,
            "categories_id": [category.id]  # List of category IDs for many-to-many
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(title="notebook")
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800)
        self.assertEqual(created_product.activate, True)