from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.cache import cache

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory

# Create your views here.


class HomeView(TitleMixin, TemplateView):
    """ Class for rendering home(index) templates """
    template_name = 'products/index.html'
    title = 'VonasahStore'


class ProductView(TitleMixin, ListView):
    """ Class for rendering products template and generate Product item list """
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Catalog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data()
        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        return context

    def get_queryset(self):
        queryset = super(ProductView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


@login_required
def basket_add(request, product_id):
    """ Class for add product to user basket or create user basket if basket does not exists """
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
