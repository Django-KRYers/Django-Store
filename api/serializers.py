from .models import Product,Cart,User
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('total_price', 'user', 'products')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'