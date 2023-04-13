from django.urls import path
from products.views import products_page_view, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', products_page_view, name='index'),
    path('category/<int:category_id>/', products_page_view, name='category'),
    path('page/<int:page_number>/', products_page_view, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]