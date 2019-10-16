from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):

    favourite_pizza = models.ForeignKey(
        'pizza_app.PizzaMenuItem', null=True, default=None, blank=True, on_delete=models.PROTECT)

    our_note = models.CharField(max_length=140, blank=True)
