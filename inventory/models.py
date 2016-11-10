from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import BaseEntity

class Category(BaseEntity):
	name = models.CharField(max_length=40)
	Parent_category = models.ForeignKey('self', related_name='sub_categories',blank=True,null=True)
	is_active = models.BooleanField(default=True)
	
	class Meta:
		abstract = False

	def __str__(self):
		return self.name
		
class Equipment(BaseEntity):
	name = models.CharField(max_length=40)
	cost = models.IntegerField()
	purchased_date = models.DateField(blank=True,null=True)
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.name