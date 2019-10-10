from django.test import TestCase

from django.contrib.auth.models import User
from order.models import Food, Order


class FoodModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Food.objects.create(
            name="Food1",
            price=100,
            sold_out=False)
    
    def test_pass(self):
        ins = Food.objects.get(name='Food1')
        self.assertEqual(ins.name, 'Food1')
        self.assertEqual(type(ins.name), str)
        self.assertEqual(ins.price, 100)
        self.assertEqual(type(ins.price), int)
        self.assertEqual(ins.sold_out, False)
        self.assertEqual(type(ins.sold_out), bool)

class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="13012345678", password="123456")
        food = Food.objects.create(name="Food1", price=100)
        Order.objects.create(
            order_number="20191010164800-0000000001",
            amount=1,
            ordered_user=user,
            ordered_food=food)

    def test_pass(self):
        ins = Order.objects.get(order_number='20191010164800-0000000001')
        self.assertEqual(ins.amount, 1)
        self.assertEqual(type(ins.amount), int)
        self.assertEqual(ins.ordered_user.username, "13012345678")
        self.assertEqual(ins.ordered_food.name, "Food1")

