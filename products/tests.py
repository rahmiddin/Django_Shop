from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from products.models import Product, ProductCategory, Basket
from users.models import User
# Create your tests here.


class HomeViewTestCase(TestCase):
    """ Test class for Home view """
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'VonasahStore')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductViewTestCase(TestCase):
    """ Test class for product view """
    fixtures = ['categories.json', 'goods.json']

    def setUp(self):
        self.products = Product.objects

    def test_product(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEquals(list(response.context_data['object_list']), list(self.products.all()[:3]))

    def test_products_category(self):
        category = ProductCategory.objects.get(id=1)
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEquals(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=1)[:3])
        )

    def _common_tests(self, response):
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')


