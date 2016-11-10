from __future__ import unicode_literals

from django.db import models

from core.models import Person

# Create your models here.
class Customer(Person):
	business_name = models.CharField(max_length=40,blank=True)
	street_name = models.CharField(max_length=40,blank=True)
	town = models.CharField(max_length=40,blank=True)
	district = models.CharField(max_length=40,blank=True)
	pin_code = models.CharField(max_length=6,blank=True)