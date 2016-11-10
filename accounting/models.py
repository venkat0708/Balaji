from __future__ import unicode_literals

from decimal import Decimal

from django.db import models

from core.models import BaseEntity
from service.models import Service, Event

# Create your models here.

CATEGORY_TYPE = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
        ('Liability', 'Liability')
    )
class Category(BaseEntity):
	type = models.CharField(max_length=30, choices = CATEGORY_TYPE, default='Income')
	name = models.CharField(max_length=40)
	Parent_category = models.ForeignKey('self', related_name='sub_categories',blank=True,null=True)
	is_active = models.BooleanField(default=True)
	
	class Meta:
		abstract = False

	def __str__(self):
		return self.name
		
class Transaction_Template(BaseEntity):
	name = models.CharField(max_length=40)
	category = models.ForeignKey('Category', related_name = 'expenses')
	is_active = models.BooleanField(default=True)
	
	class Meta:
		abstract = False

	def __str__(self):
		return self.name
		
class Transaction(BaseEntity):
	name = models.ForeignKey('Transaction_Template', related_name = 'transactions')
	description = models.CharField(max_length = 100)
	amount = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	event = models.ForeignKey('service.Event', related_name='transactions',blank=True,null=True)
	service = models.ForeignKey('service.Service',related_name='transactions',blank=True,null=True)
	
	class Meta:
		abstract = False

	def __str__(self):
		return self.name