from django.db import models

# Create your models here.
class user (models.Model):
    userid = models.IntegerField()
    pass1 = models.TextField(max_length=15)
    username = model.models.CharField(max_length=50)
    userbalance = model.models.IntegerField()


