from django.db import models

# Create your models here.
class Logs(models.Model):
    c_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    code = models.IntegerField()
    status = models.CharField(max_length=100)

class UserLogin(models.Model):
    l_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    l_ip = models.CharField(max_length=16)
    l_user = models.CharField(max_length=64)

class UserHandle(models.Model):
    h_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    h_user_index = models.IntegerField()
    h_index = models.IntegerField()
    handle = models.CharField(max_length=512)
    h_user_login = models.IntegerField()