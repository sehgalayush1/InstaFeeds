from __future__ import unicode_literals

from django.db import models
from college import models as college_models

class Society(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    link = models.CharField(max_length=100)
    icon = models.ImageField(max_length=200)
    created_date = models.DateTimeField('created date')
    college_id = models.ForeignKey(college_models.College)
    department = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.name

