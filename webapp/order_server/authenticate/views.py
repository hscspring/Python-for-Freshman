import json

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


from django.views import View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework.response import Response


from authenticate.models import UserProfile
from authenticate.serializers import UserSerializer
from authenticate.serializers import MyTokenObtainPairSerializer


class ListUserView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignUpView(View):

    greeting = "Hello, POST needed"

    def get(self, request):
        return HttpResponse(self.greeting)

    def post(self, request):
        info = json.loads(request.body)
        try:
            phone = info["phone"]
            password = info["password"]
            identity = info.get("identity", 0)
            nickname = info.get("nickname", "")
        except KeyError as e:
            return JsonResponse({"error_code": 10001,
                                 "error_msg": "parameter error"})
        # if use get, should use try...except...
        up = UserProfile.objects.filter(phone=phone)
        if up:
            return JsonResponse({"error_code": 10000,
                                 "error_msg": "user exist"})
        else:
            user = User(username=phone)
            user.password = make_password(password)
            user.save()
            up = UserProfile()
            up.user = user
            up.nickname = nickname
            up.phone = phone
            up.identity = identity
            up.save()
        return JsonResponse({"data": "success"})
