from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):

    name = models.CharField("菜名", max_length=100, null=False, blank=False)
    price = models.IntegerField("价格", null=False, blank=False)
    sold_out = models.BooleanField("是否售罄", default=False, null=False, blank=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)

    def __str__(self):
        return self.name + "-" + str(self.price)


class Order(models.Model):
    order_number = models.CharField("订单编号", max_length=100, null=False, blank=False)
    amount = models.SmallIntegerField("份数", default=1, null=False, blank=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)
    ordered_user = models.ForeignKey(User, verbose_name="下单用户", on_delete=models.CASCADE)
    ordered_food = models.ForeignKey(Food, verbose_name="下单菜品", on_delete=models.CASCADE)
