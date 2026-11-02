from django.contrib import admin
from .models import Customer, NextPerson, Blog


admin.site.register(Customer)
admin.site.register(NextPerson)
admin.site.register(Blog)
# Register your models here.
