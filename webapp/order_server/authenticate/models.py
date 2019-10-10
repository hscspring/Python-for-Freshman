from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    IDENTITY = ((0, "普通用户"), (1, "VIP"), (2, "VVIP"))

    user = models.OneToOneField(User, verbose_name="用户信息", on_delete=models.CASCADE)
    nickname = models.CharField("昵称", max_length=100, blank=True, null=True)
    phone = models.CharField("手机号", unique=True, max_length=16)
    identity = models.SmallIntegerField("身份", choices=IDENTITY, default=0)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)

    def __str__(self):
        return self.nickname + "-" + self.phone
