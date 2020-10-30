from django.contrib import admin
from .models import Product, Characteristic, Stand, Order

# Add models to django admin
admin.site.register(Product)
admin.site.register(Characteristic)
admin.site.register(Stand)
admin.site.register(Order)
