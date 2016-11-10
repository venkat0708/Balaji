from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):

	fieldsets = [
		('personal', {'fields':['first_name','last_name','contact_number']}),
		('Address', {'fields':['business_name','street_name','town','district','pin_code']})
	]
	list_display = ('first_name','last_name','contact_number','business_name','town')
	search_fields = ['first_name','business_name','contact_number']
	list_filter = ['town']
admin.site.register(Customer, CustomerAdmin)