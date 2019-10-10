import json

from django.test import Client, TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import force_authenticate

from django.contrib.auth.hashers import make_password
from django.urls import reverse

from django.contrib.auth.models import User
from authenticate.models import UserProfile


class SignUpViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # `create` automacally save instance
        cls.user = User.objects.create(username="13012345678",
                                       password=make_password("123456"))
        cls.ins = UserProfile(
            user=cls.user,
            nickname="Test0",
            phone="13012345678",
            identity=0)
        cls.ins.save()

    def setUp(self):
        self.client_unauth = Client()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_list_pass(self):
        response = self.client.get('/api/auth/users/')
        self.assertEqual(response.status_code, 200)

    def test_user_detail_pass(self):
        url = reverse('user_detail', args=(self.ins.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_fail(self):
        url = reverse('user_detail', args=(10000, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_sign_up(self):
        req = {
            "phone": "13112345678",
            "password": "123456",
            "identity": 1,
            "nickname": "Test1"
        }
        response = self.client_unauth.post(
            '/api/auth/sign_up/', data=req, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['data'], "success")
        select = UserProfile.objects.get(phone="13112345678")
        assert select.identity == 1
        assert select.nickname == "Test1"


    def test_sign_up_without_not_must_params(self):
        req = {
            "phone": "13212345678",
            "password": "123456",
        }
        response = self.client_unauth.post(
            '/api/auth/sign_up/', data=req, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['data'], "success")
        select = UserProfile.objects.get(phone="13212345678")
        assert select.identity == 0
        assert select.nickname == ""

    def test_sign_up_without_must_params(self):
        req = {
            "phone": "13312345678"
        }
        response = self.client_unauth.post(
            '/api/auth/sign_up/', data=req, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['error_code'], 10001)
        self.assertIn("parameter", content['error_msg'])
        select = UserProfile.objects.filter(phone="13312345678")
        assert list(select) == []

    def test_sign_up_already_exist(self):
        req = {
            "phone": "13012345678",
            "password": "123456",
        }
        response = self.client_unauth.post(
            '/api/auth/sign_up/', data=req, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['error_code'], 10000)
        self.assertIn("exist", content['error_msg'])



    