from django.contrib import admin

# Register your models here.
from .models import Service,Event, ServiceBooking

class ServiceBookingInline(admin.TabularInline):
	model = ServiceBooking
	extra = 3
	
class EventAdmin(admin.ModelAdmin):
	fieldsets = [
			('Basic', {'fields':['name','customer','venue']}),
			('Timing', {'fields':['start_datetime','end_datetime']}),
			('Payment', {'fields':['total','paid','due']})
	]
	
	list_display = ('name','customer','start_datetime','end_datetime','total','paid','due')
	list_filter = ['customer','start_datetime']
	search_fields = ['customer','name']
	
	inlines = [ServiceBookingInline]

class ServiceBookingAdmin(admin.ModelAdmin):

	list_display = ('event','service','status','price')
	list_filter = ['service','status']
	search_fields = ['event','service']
	
class ServiceAdmin(admin.ModelAdmin):
	
	list_display = ('name','price','is_active')
	list_filter = ['is_active']
	search_fields = ['name']

	
admin.site.register(Service, ServiceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(ServiceBooking, ServiceBookingAdmin)