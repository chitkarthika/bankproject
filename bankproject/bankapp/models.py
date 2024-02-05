from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=50)
    wikilink=models.CharField(max_length=300,null=True,blank=True)
   # class Meta:
       # ordering=('name')
      #  verbose_name='district'
      #  verbose_name_plural='districts'

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    gender= models.CharField(max_length=100)
    age=models.IntegerField()
    phno=models.IntegerField()
    email=models.CharField(max_length=20)
    address= models.TextField(max_length=300)
    account=models.CharField(max_length=100)
    material=models.CharField(max_length=300)

    def __str__(self):
        return self.name