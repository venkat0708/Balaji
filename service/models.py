from __future__ import unicode_literals

from decimal import Decimal

from django.db import models

from core.models import BaseEntity
from customers.models import Customer
# Create your models here.



STATUS_EVENTS = (
        ('Booked', 'Booked'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
		('Completed', 'Completed'),
    )

class Service(BaseEntity):
	name = models.CharField(max_length=40)
	price = models.IntegerField()
	is_active = models.BooleanField(default=True)
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.name
		
class ServiceBooking(BaseEntity):
	service = models.ForeignKey('Service', related_name='bookings')
	status = models.CharField(max_length=30, choices = STATUS_EVENTS, default='Booked')
	price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	event = models.ForeignKey('Event', related_name='services')	
	
	
class Event(BaseEntity):
	name = models.CharField(max_length=40)
	venue = models.CharField(max_length=100,blank=True,null=True)
	start_datetime = models.DateTimeField(blank=True,null=True)
	end_datetime = models.DateTimeField(blank=True,null=True)
	status = models.CharField(max_length=30, choices = STATUS_EVENTS, default='Booked')
	customer = models.ForeignKey('customers.Customer',related_name='events',blank=True,null=True)
	total = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	paid = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)
	due = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),blank=True,null=True)
	
	class Meta:
		abstract = False
	
	def __str__(self):
		return self.name