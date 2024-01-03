from django.shortcuts import render

from catalog.models import Category, Product
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Category, Product


def index(request):
    products = Product.objects.all()

    for product in products:
        if len(product.description) > 100:
            product.description = product.description[:100] + '...'

    context = {
        'products': products,
    }
    return render(request, 'catalog/index.html', context)


class ContactsView(View):
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
        return HttpResponseRedirect('/')

    def get(self, request):
        return render(request, 'catalog/contacts.html')


class CatalogItemsView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'categories': categories,
            'products': products,
        }
        return render(request, 'catalog/catalog_items.html', context)


class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'catalog/product_detail.html', {'product': product})
