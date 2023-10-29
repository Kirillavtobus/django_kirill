from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    nodified_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Birthday = models.CharField(max_length=30)
    age = models.CharField(max_length=2)
    email = models.CharField(max_length=100)


