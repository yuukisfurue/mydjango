from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator  #☆

class Member(models.Model):
    name = models.CharField(verbose_name="名前",max_length=100)
    prefecture  = models.CharField(verbose_name="出身地",choices=settings.PREFECTURES,max_length=100)
    gender  = models.CharField(verbose_name="性別",choices=settings.GENDERS,max_length=100)
    employmentstatus  = models.CharField(verbose_name="雇用形態",choices=settings.EMPLOYMENTSTATUSS,max_length=100)
    company= models.CharField(verbose_name="業種",choices=settings.COMPANYS,max_length=100)
    jyob  = models.CharField(verbose_name="配属部署",choices=settings.JYOBS,max_length=100) 
    stay= models.CharField(verbose_name="現住所",choices=settings.STAYS,max_length=100)
    affiliation  = models.CharField(verbose_name="所属先",choices=settings.AFFILIATONS,max_length=100)
    postion  = models.CharField(verbose_name="現役職",choices=settings.POSITIONS,max_length=100)
    annual  = models.CharField(verbose_name="今年(万)",choices=settings.ANNUALS,max_length=100) 
    lastyear  = models.CharField(verbose_name="昨年(万)",choices=settings.LASTYEARS,max_length=100)
    
    def __str__(self):
        return '<Member:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.name) + ')>'

class Plofile(models.Model):            
    name = models.CharField(verbose_name="名前",max_length=100)
    prefecture  = models.CharField(verbose_name="出身地",choices=settings.PREFECTURES,max_length=100)
    gender  = models.CharField(verbose_name="性別",choices=settings.GENDERS,max_length=100)
    employmentstatus  = models.CharField(verbose_name="雇用形態",choices=settings.EMPLOYMENTSTATUSS,max_length=100)
    company= models.CharField(verbose_name="業種",choices=settings.COMPANYS,max_length=100)
    jyob  = models.CharField(verbose_name="配属部署",choices=settings.JYOBS,max_length=100) 
    stay= models.CharField(verbose_name="現住所",choices=settings.STAYS,max_length=100)
    affiliation  = models.CharField(verbose_name="所属先",choices=settings.AFFILIATONS,max_length=100)
    postion  = models.CharField(verbose_name="現役職",choices=settings.POSITIONS,max_length=100)
    annual  = models.CharField(verbose_name="今年(万)",choices=settings.ANNUALS,max_length=100) 
    lastyear  = models.CharField(verbose_name="昨年(万)",choices=settings.LASTYEARS,max_length=100)
