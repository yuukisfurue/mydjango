import re
from django.db import models
from django.core.validators import ValidationError

def number_only(value):
    if (re.match(r'^[0-9]*$', value) == None):
        raise ValidationError(
            '%(value)s is not Number!', \
            params={'value': value},
        )

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=200)
    pref = models.CharField(max_length=200)
    jyob = models.CharField(max_length=200)
    pojishon = models.CharField(max_length=200)
     
    def __str__(self):
        return '<Member:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'