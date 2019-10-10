import json

from django.test import Client, TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import force_authenticate

from django.contrib.auth.hashers import make_password
from django.urls import reverse

from django.contrib.auth.models import User
from authenticate.models import UserProfile
from order.models import Food, Order


class ShowMenuViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ins = Food.objects.create(
            name="Food1",
            price=100,
            sold_out=False)
        cls.user = User.objects.create(
            username="13012345678", password=make_password("123456"))
        UserProfile.objects.create(
            user=cls.user,
            nickname="Test1",
            phone="13012345678",
            identity=0)

    def setUp(self):
        self.client_unauth = Client()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_food_list_pass(self):
        response = self.client.get('/api/order/food/')
        self.assertEqual(response.status_code, 200)

    def test_food_detail_pass(self):
        url = reverse('food_detail', args=(self.ins.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_fail(self):
        url = reverse('food_detail', args=(10000, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_show_menu(self):
        response = self.client.get('/api/order/show_menu/')
        assert self.user.id == 1
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        assert type(content['menu']) == list

    def test_show_menu_not_login(self):
        response = self.client_unauth.get('/api/order/show_menu/')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Authentication", content['detail'])


class SubmitViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ins1 = Food.objects.create(
            name="Food1",
            price=100,
            sold_out=False)
        cls.ins2 = Food.objects.create(
            name="Food2",
            price=200,
            sold_out=False)
        cls.ins3 = Food.objects.create(
            name="Food3",
            price=300,
            sold_out=True)

        cls.user = User.objects.create(
            username="13012345678", password=make_password("123456"))
        UserProfile.objects.create(
            user=cls.user,
            nickname="Test1",
            phone="13012345678",
            identity=0)
        cls.ins = Order.objects.create(
            order_number="20191010164800-0000000001",
            amount=1,
            ordered_user=cls.user,
            ordered_food=cls.ins1)

    def setUp(self):
        self.client_unauth = Client()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_order_list_pass(self):
        response = self.client.get('/api/order/orders/')
        self.assertEqual(response.status_code, 200)

    def test_order_detail_pass(self):
        url = reverse('order_detail', args=(self.ins.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_fail(self):
        url = reverse('order_detail', args=(10000, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_submit(self):
        req = {
            "ordered_food": [{"food_id": 1, "amount": 1},
                             {"food_id": 2, "amount": 2}]
        }
        response = self.client.post(
            '/api/order/submit_order/', req, format='json')
        assert self.user.id == 1
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        assert type(content['order_number']) == str
        select = Order.objects.filter(order_number=content['order_number'])
        order1 = list(select)[0]
        assert order1.amount == 1
        assert order1.ordered_user.username == "13012345678"
        assert order1.ordered_food.name == "Food1"

    def test_submit_not_login(self):
        req = {
            "ordered_food": [{"food_id": 1, "amount": 1},
                             {"food_id": 2, "amount": 2}]
        }
        response = self.client_unauth.post(
            '/api/order/submit_order/',
            data=req, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Authentication", content['detail'])
