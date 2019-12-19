from django.db import models

# Create your models here.
class Logs(models.Model):
    c_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    code = models.IntegerField()
    status = models.CharField(max_length=100)
