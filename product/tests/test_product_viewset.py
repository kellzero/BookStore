import pytest
from rest_framework.test import APIClient
from rest_framework import status
from product.factories import ProductFactory, UserFactory


class TestProductViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        yield
        self.client.force_authenticate(user=None)

    @pytest.mark.django_db
    def test_create_product(self):
        data = {
            "title": "Novo Produto",
            "description": "Descrição do novo produto",
            "price": 1999,
            "activate": True,
            "category": []
        }

        # Use a URL correta - note o 'api/' no início
        response = self.client.post('/api/products/', data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == data['title']

    @pytest.mark.django_db
    def test_list_products(self):
        # Create some test products
        ProductFactory.create_batch(3)

        response = self.client.get('/api/products/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 3