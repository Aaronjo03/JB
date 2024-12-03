from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Sauce)
admin.site.register(Topping)
admin.site.register(Cheese)
admin.site.register(Pizza)
admin.site.register(CustomerInfo)