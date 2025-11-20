from rest_framework import serializers
from product.models import Product
from .category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'activate', 'category']
        extra_kwargs = {
            'category': {'required': False}  # Torna o campo opcional
        }

    # Ou se você quiser representar as categorias como dados aninhados:
    # category = CategorySerializer(many=True, read_only=True)