from django.db import models


class registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    again_password = models.CharField(max_length=100)

