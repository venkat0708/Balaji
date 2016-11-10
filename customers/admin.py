from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):

	fieldsets = [
		('personal', {'fields':['first_name','last_name','contact_number']}),
		('Address', {'fields':['business_name','street_name','town','district','pin_code']})
	]

admin.site.register(Customer, CustomerAdmin)