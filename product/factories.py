import factory
from factory.django import DjangoModelFactory
from product.models import Product
from product.models import Category
from django.contrib.auth.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.Faker('random_number', digits=2)
    activate = True