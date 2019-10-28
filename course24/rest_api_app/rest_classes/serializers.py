# -*- coding: utf-8 -*-

from rest_framework import serializers

from pizza_auth_app.models import CustomUser
from pizza_app.models import PizzaMenuItem, PizzaIngredient


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class is used to get the pizza menu items.
    But it does not show ingredients.

    TODO: add ingredients
    """

    class Meta:
        model = PizzaMenuItem
        fields = ('id', 'name', 'ingredients')

    ingredients = serializers.PrimaryKeyRelatedField(many=True,
                                                     queryset=PizzaIngredient.objects.all())


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class is used to show users, but favourite_pizza can not be saved.

    TODO: add possibility to save favourite_pizza
    """
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'our_note',
            'favourite_pizza',
        )

    # favourite_pizza = PizzaMenuItemSerializer(required=False)
    favourite_pizza = serializers.SlugRelatedField(
        slug_field='name',
        queryset=PizzaMenuItem.objects.all(),
        # allow_null = True
     )
