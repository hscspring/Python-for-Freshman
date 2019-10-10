from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authenticate.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'identity', 'phone']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # data['user_id'] = self.user.id
        up = UserProfile.objects.get(phone=self.user.username)
        data['nickname'] = up.nickname

        return data
