from __future__ import unicode_literals

from django.db import models

class College(models.Model):
    name= models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    link =models.CharField(max_length=100)
    icon=models.ImageField(max_length=200)
    coverImage=models.ImageField(max_length=200)

    def __str__(self):
    	return self.name

