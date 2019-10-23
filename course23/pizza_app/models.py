from django.conf import settings
from django.db import models
from django.db.models import Manager
from django.utils import timezone
from django.db.models.signals import post_save, m2m_changed
from django.utils.text import get_valid_filename


class Address(models.Model):
    full = models.CharField(max_length=150)

    def __str__(self):
        return str(self.full)


class PizzaIngredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class PizzaMenuItem(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        'PizzaIngredient',
        related_name='ingredients'
    )

    def __str__(self):
        return str(self.name)


class PizzaSize(models.Model):
    LARGE = ('XL', 'Large')
    MEDIUM = ('MD', 'Medium')
    SMALL = ('SM', 'Small')
    __all = dict([LARGE, MEDIUM, SMALL])

    size = models.CharField(max_length=2, choices=__all.items())

    def __str__(self):
        return str(self.__all[self.size])


class PizzaOrderManager(Manager):
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            delivered=True,
        )


class PizzaOrderUndeliveredManager(Manager):
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            delivered=False,
        )


class PizzaOrder(models.Model):
    rel_name = 'pizzas'
    # Linking:
    kind = models.ForeignKey('PizzaMenuItem', related_name='pizzas', on_delete=models.PROTECT)
    size = models.ForeignKey('PizzaSize', related_name='pizzas', on_delete=models.PROTECT)
    delivery = models.ForeignKey('Address', related_name='pizzas', on_delete=models.PROTECT)

    # Buisness logic:
    extra = models.ManyToManyField(
        'PizzaIngredient', blank=True, related_name='pizzas_extras')
    exclude = models.ManyToManyField('PizzaIngredient', blank=True)
    comment = models.CharField(max_length=140, blank=True)

    # Utils:
    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(default=None, null=True)

    objects = Manager()
    delivered_manager = PizzaOrderManager()
    undelivered_manager = PizzaOrderUndeliveredManager()

    def mark_delivered(self, commit=True):
        self.delivered = True
        self.date_delivered = timezone.now()
        if commit:
            self.save()

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new PizzaOrder!')
        else:
            print('Updating the existing one')

        super(PizzaOrder, self).save(**kwargs)

    def __str__(self):
        return 'PizzaOrder [%s]' % self.id
