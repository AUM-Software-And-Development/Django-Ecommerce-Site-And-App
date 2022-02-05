import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce_project.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=models.Category

    # Appends random elements to a name
    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")

register(CategoryFactory)
