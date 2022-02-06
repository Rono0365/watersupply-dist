from django.db import models

# Created my water model here.
class Reading(models.Model):
    name_of_project = models.CharField(max_length=100,default='')
    elect_consumption = models.CharField(max_length=100,default='')
    waterconsp = models.CharField(max_length=100,default='')
    meterread = models.CharField(max_length=100,default='')#per unit meter
        
    
