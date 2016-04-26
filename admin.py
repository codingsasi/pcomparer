from django.contrib import admin
from .models import Product, Category, Vendor

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Vendor)
