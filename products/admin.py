from django.contrib import admin

from products.views import Basket, Product, ProductCategory

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description',
              ('price', 'quantity'),
              'image', 'category')
    search_fields = ('name', )
    ordering = ('category', )


admin.site.register(ProductCategory)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', )
    extra = 0
