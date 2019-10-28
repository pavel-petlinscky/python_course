# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.
from pizza_app.models import PizzaSize, PizzaIngredient, Address


class TestPizzaSize(TestCase):
    def test_pizza_size_creation(self):
        pizza_size = PizzaSize.objects.create(
            size=PizzaSize.SMALL[0])
        assert pizza_size.pk is not None

    # def test_fail(self):
    #     assert True == False


class TestPizzaIngredient(TestCase):
    @classmethod
    def setUp(cls):
        cls.address = Address.objects.create(
            full='Russia, Moscow')

    def test_pizza_create_ingredient(self):
        ing = PizzaIngredient.objects.create(name='test')
        assert ing.pk is not None

    def test_pizza_get_ingredient(self):
        ing = PizzaIngredient.objects.get(name='Ham')
        assert ing is not None


# TODO: add tests for PizzaOrder
