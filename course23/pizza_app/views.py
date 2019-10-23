from django.urls import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from pizza_app.models import PizzaOrder, PizzaSize
from pizza_app.forms import PizzaOrderForm, DeliveryForm


# Create your views here.


def index(request):
    if request.method == 'GET':
        pizzas = PizzaOrder.objects.all()
        return render(request, 'pizza_app/index.html', {'pizzas': pizzas})
    return HttpResponse(status=405)


def create(request):
    if request.method == 'GET':
        c = {
            'pizza_form': PizzaOrderForm(),
            'delivery_form': DeliveryForm(),
        }
        return render(request, 'pizza_app/create.html', c)

    elif request.method == 'POST':
        pizza_form = PizzaOrderForm(request.POST)
        delivery_from = DeliveryForm(request.POST)

        if pizza_form.is_valid() and delivery_from.is_valid():
            with transaction.atomic():
                delivery = delivery_from.save()
                pizza = pizza_form.save(delivery=delivery)
                pizza_form.save_m2m()

            return redirect(reverse('pizza:view', kwargs={
                'pizza_order_id': pizza.pk
            }))
        else:
            c = {
                'pizza_form': pizza_form,
                'delivery_form': delivery_from,
            }
            return render(request, 'pizza_app/create.html', c)
    return HttpResponse(status=405)


def view(request, pizza_order_id):
    if request.method == 'GET':
        # pizza = get_object_or_404(PizzaOrder, id=pizza_order_id)

        # pizza = PizzaOrder.objects.filter(id=pizza_order_id).first()
        # pizza = PizzaOrder.objects.select_related().filter(id=pizza_order_id).first()
        pizza = PizzaOrder.objects.select_related('kind').filter(id=pizza_order_id).first()
        # pizza = PizzaOrder.objects.select_related()\
        #     .prefetch_related()\
        #     .filter(id=pizza_order_id)\
        #     .first()
        # pizza = PizzaOrder.objects\
        #     .select_related()\
        #     .prefetch_related('extra', 'exclude')\
        #     .filter(id=pizza_order_id).first()

        if not pizza:
            raise Http404

        return render(request, 'pizza_app/view.html', {'pizza': pizza})
    return HttpResponse(status=405)


def close(request, pizza_order_id):
    if request.method == 'GET':
        try:
            pizza = get_object_or_404(PizzaOrder, id=pizza_order_id)
            pizza.mark_delivered()

            return redirect(reverse('pizza:view', kwargs={
                'pizza_order_id': pizza.pk
            }))
        except PizzaOrder.DoesNotExist:
            return HttpResponse('Does not exist', status_code=404)
    return HttpResponse(status=405)


def stats(request):
    if request.method == 'GET':
        count = PizzaOrder.objects.count()
        average_extras = PizzaOrder.objects.all().annotate(
            extra_count=Count('extra')
        ).aggregate(result=Avg('extra_count'))

        small_size = PizzaSize.objects.get(
            size=PizzaSize.SMALL[0]
        )
        small_pizzas = PizzaOrder.objects.filter(
            size=small_size
        )

        small_pizzas = PizzaOrder.objects.filter(
            size__size=PizzaSize.SMALL[0],
        )

        print(list(small_pizzas))
        print(repr(PizzaOrder.objects))
        s = PizzaOrder

        today = timezone.now()
        query = {
            'date_created__day': today.day,
            'date_created__month': today.month,
            'date_created__year': today.year,
        }
        today_pizzas = PizzaOrder.objects.filter(
            **query
        ).count()

        today_delivered = PizzaOrder.delivered_manager.filter(
            # delivered=True,  # TODO: manager
            **query
        ).count()

        # Try these lines with PostgreSQL:
        # average_delivery_time = PizzaOrder.objects.filter(
        #     delivered=True,
        # ).annotate(
        #     diff=F('date_delivered') - F('date_created')
        # ).aggregate(result=Avg('diff'))

        params = {
            'count': count,
            'average_extras': average_extras['result'],
            'today_pizzas': today_pizzas,
            'today_delivered': today_delivered,
            'average_delivery_time': 'not available with sqlite',
        }

        return render(request, 'pizza_app/stats.html', {'params': params})
    return HttpResponse(status=405)
