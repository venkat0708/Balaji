from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseEntity(models.Model):
	created_date = models.DateTimeField(auto_now_add = True)
	updated_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

class Person(BaseEntity):
	first_name = models.CharField(max_length=40,null=True,blank=True)
	last_name = models.CharField(max_length=40,blank=True,null=True)
	contact_number = models.CharField(max_length=10,blank=True,null=True)
	
	class Meta:
		abstract = True
	
	
	def __str__(self):
		return ' '.join([self.first_name, self.last_name])