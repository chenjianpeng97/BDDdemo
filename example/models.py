from django.db import models


# Create your models here.
class User(models.Model):
    # 用户名
    name = models.CharField(max_length=20)
    # 角色
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
# class Account
