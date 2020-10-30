from django.db import models
from django.contrib.auth.models import User


class Stand(models.Model):
    """
    Stand model that can be associated with different products
    """
    # auto id
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model where each stand has N products
    and each product belogs to 1 stand
    """
    # auto id
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    """
    Characteristic model where a product can have N characteristics
    and a characteristic can be associated with 1 product
    """
    # auto id
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Order model where a order can have 1 characteristic associated already
    with a product and 1 user
    """
    # auto id
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='only_user')
    product = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='only_product')
