from django.db import models


class registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    again_password = models.CharField(max_length=100)


class Foods(models.Model):
    name = models.CharField(max_length=30)
    food_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.CharField(max_length=50)


class Parlor(models.Model):
    name = models.CharField(max_length=30)
    expert = models.TextField()
    charge = models.CharField(max_length=20)


class Tutor(models.Model):
    name = models.CharField(max_length=30)
    expert = models.TextField()
    charge = models.CharField(max_length=20)

