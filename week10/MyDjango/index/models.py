from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

# Create your models here.
class Indexmodels.Model):
    id = models.BigAutoField(primary_key = True)
    date = models.CharField(max_length = 30)
    n_star = models.IntegerField()
    sum_i = models.IntegerField()
    link = models.CharField(max_length=40)
    estimate = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=11,decimal_places = 10)


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, phone=None, email=None):
        User = get_user_model()
        if username and password:
            user = super().authenticate(request, username=username, password=password)
            print('==账号==')
            if user:
                return user
        elif email and password:
                print('==邮箱==')
                user = User.objects.filter(Q(email=email )).first()
                # print(user)
                if user:
                    print('==密码==')
                    if user.check_password(password) and self.user_can_authenticate(user):
                        return user
                    else:
                        print('===', user.check_password(password))