from django.contrib.auth.decorators import login_required
from django.urls import path

from products.views import ProductView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', login_required(basket_add), name='basket_add'),
    path('baskets/remove/<int:basket_id>/', login_required(basket_remove), name='basket_remove'),
]
