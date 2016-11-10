from django.contrib import admin

# Register your models here.
from .models import Service,Event, ServiceBooking

admin.site.register(Service)
admin.site.register(Event)
admin.site.register(ServiceBooking)