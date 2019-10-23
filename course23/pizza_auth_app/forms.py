# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm

from pizza_auth_app.models import CustomUser


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', )
