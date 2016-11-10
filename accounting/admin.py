from django.contrib import admin

# Register your models here.
from .models import Category, Transaction_Template,Transaction

admin.site.register(Category)
admin.site.register(Transaction_Template)
admin.site.register(Transaction)