# -*- coding: utf-8 -*-

from pizza_project.celery_app import app
from pizza_app.models import PizzaOrder


@app.task
def greet_new_orders():
    print('welcome, new orders!')
    return 'greet new orders result'


@app.task
def order_created(order_id):
    order = PizzaOrder.objects.get(pk=order_id)
    print('this task will do some background work')
    return 'background result. comment: %s' % order.comment
