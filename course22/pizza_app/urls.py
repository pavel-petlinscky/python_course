from django.urls import path

from pizza_app.views import create, view, close, stats

app_name = 'pizza_app'

urlpatterns = [
    path('create/', create, name='create'),
    # # view/<int:pizza_order_id>
    path('view/<int:pizza_order_id>/', view, name='view'),
    path('close/<int:pizza_order_id>/', close, name='close'),
    #
    path('stats/', stats, name='stats'),
]
