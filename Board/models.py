from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    pref = models.CharField(max_length=200)
    jyob = models.CharField(max_length=200)
    pojishon = models.CharField(max_length=200)