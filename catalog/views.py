
from catalog.forms import ModeratorProductForm, ProductForm
from catalog.models import Category, Product
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
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


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Поменяйте на правильное имя пространства имен и представления
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ModeratorProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:list')  # Поменяйте на 'product:list'
    else:
        form = ModeratorProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


def product_delete(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('product:list')  # Поменяйте на 'product:list'


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})
