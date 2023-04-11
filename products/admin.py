from django.contrib import admin
from products.views import Product, ProductCategory
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)