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
    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")

register(CategoryFactory)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug=fake.lexify(text="prod_slug_??????")
    name=fake.lexify(text="prod_name_??????")
    description=fake.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)

register(ProductFactory)
