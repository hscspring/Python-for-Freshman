from django.test import TestCase

from django.contrib.auth.models import User
from authenticate.models import UserProfile



class UserProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="13012345678", password="123456")
        UserProfile.objects.create(
            user=user,
            nickname="Test1",
            phone="13012345678",
            identity=0)

    def test_discrib(self):
        user = User.objects.create(username="13112345678", password="123456")
        ins = UserProfile.objects.create(
            user=user,
            nickname="Test2",
            phone="13112345678",
            identity=1)
        assert str(ins) == "Test2-13112345678"


    def test_nickname(self):
        ins = UserProfile.objects.get(nickname='Test1')
        expected_object = ins.nickname
        self.assertEqual(expected_object, 'Test1')
        self.assertEqual(type(expected_object), str)

    def test_phone(self):
        ins = UserProfile.objects.get(phone='13012345678')
        expected_object = ins.phone
        self.assertEqual(expected_object, '13012345678')
        self.assertEqual(type(expected_object), str)
