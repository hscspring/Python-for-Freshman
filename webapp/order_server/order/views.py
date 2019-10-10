import json
import datetime

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views import View
from django.http import JsonResponse, HttpResponse

from order.models import Order, Food
from order.serializers import FoodSerializer, OrderSerializer
from order.config import DISCOUNT

from django.contrib.auth.models import User

from authenticate.models import UserProfile


class ListFoodView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class DetailFoodView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class ListOrderView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrderView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ShowMenuView(APIView):

    def get(self, request):
        # see https://www.django-rest-framework.org/api-guide/authentication/
        # request.user.get_username()
        # user_id = request.GET["user_id"]
        user_id = request.user.id
        try:
            up = UserProfile.objects.get(user_id=user_id)
            discount = DISCOUNT.get(up.identity, 1.0)
            menu = Food.objects.all()
            order_list = self.print_menu(list(menu), discount)
            return JsonResponse({"menu": order_list})
        except Exception as e:
            return JsonResponse({"error_code": 10002,
                                 "error_msg": "invalid user"})

    def print_menu(self, menu: list, discount: float):
        res = []
        for food in menu:
            price = food.price * discount
            res.append((food.id, food.name, price, food.sold_out))
        return res


class SubmitView(APIView):

    greeting = "Hello, POST needed"

    def post(self, request):
        info = json.loads(request.body)
        ordered_food = info.get("ordered_food")
        user_id = request.user.id
        
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        order_number = "-".join((now, str(user_id).zfill(10)))
        
        user = User.objects.get(id=user_id)
        if user:
            ordered_user = user
        else:
            return JsonResponse({"error_code": 10002,
                                 "error_msg": "invalid user"})
        for item in ordered_food:
            food_id = int(item.get("food_id"))
            amount = int(item.get("amount", 1))
            food = Food.objects.get(id=food_id)
            if food:
                ordered_food = food
            else:
                return JsonResponse({"error_code": 10001,
                                     "error_msg": "parameter error"})
            order = Order()
            order.order_number = order_number
            order.amount = amount
            order.ordered_user = ordered_user
            order.ordered_food = ordered_food
            order.save()

        return JsonResponse({"order_number": order_number})
