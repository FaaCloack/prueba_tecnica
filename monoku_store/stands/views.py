from django.contrib.auth.models import User
from stands.models import Stand, Product, Characteristic, Order
from rest_framework import viewsets
from stands.serializers import StandSerializer, ProductSerializer, CharacteristicSmallSerializer, OrderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to see the list of stands
    or filter by id
    """
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to see the list of products
    or filter by id
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CharacteristicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to see the list of characteristic
    or filter by id
    """
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSmallSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to see the list of orders
    or filter by id
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
