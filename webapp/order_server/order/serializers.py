from rest_framework import serializers

from order.models import Food, Order


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'sold_out', 'create_time']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'ordered_user',
                  'ordered_food', 'amount', 'create_time']
