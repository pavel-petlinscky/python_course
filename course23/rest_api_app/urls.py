# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from rest_api_app.rest_classes.views import (
    UserViewSet,
    PizzaMenuItemViewSet,
)

app_name = 'rest_api_app'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pizzamenuitem', PizzaMenuItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
