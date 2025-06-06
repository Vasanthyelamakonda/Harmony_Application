from tkinter.constants import CASCADE
from turtledemo.penrose import start

from django.db import models

# Create your models here.

class users(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=40)
    password=models.CharField(max_length=12)
    gender=models.CharField(max_length=2)
    languages=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=5)
    phone_number=models.IntegerField()
    email=models.CharField(max_length=40)


class admin(models.Model):
    slno=models.IntegerField(primary_key=True)
    admin_id=models.CharField(max_length=30)
    password=models.CharField(max_length=12)


class state(models.Model):
    state_id=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=30)

class city(models.Model):
    city_id=models.IntegerField(primary_key=True)
    city_name=models.CharField(max_length=30)
    state_id=models.ForeignKey(state, on_delete=models.CASCADE)

class bloodgroup(models.Model):
    Bid=models.IntegerField(primary_key=True)
    bloodgroup_name=models.CharField(max_length=15)
