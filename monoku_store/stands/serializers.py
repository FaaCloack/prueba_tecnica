from rest_framework import serializers
from .models import Stand, Product, Characteristic, Order
from django.contrib.auth.models import User


class CharacteristicSmallSerializer(serializers.ModelSerializer):
    """
    Characteristic detail serializer, nested display
    """
    class Meta:
        model = Characteristic
        fields = ['product', 'id', 'name', 'description']


class ProductSmallSerializer(serializers.ModelSerializer):
    """
    Product detail serializer, nested display
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    """
    Product serializer
    """
    # stores the characteristics of a product
    characteristics = CharacteristicSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['stand', 'id', 'name', 'description', 'characteristics']


class StandSerializer(serializers.ModelSerializer):
    """
    Stand serializer
    """
    # stores the products of a stand
    products = ProductSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Stand
        fields = ['id', 'name', 'description', 'products']


class OrderSerializer(serializers.ModelSerializer):
    """
    Order serializer
    """

    class Meta:
        model = Order
        fields = '__all__'
