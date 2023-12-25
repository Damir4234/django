from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    products = Product.objects.all()

    for product in products:
        if len(product.description) > 100:
            product.description = product.description[:100] + '...'

    context = {
        'products': products,
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')


def catalog_items(request):
    categories = Category.objects.all()  # Получение всех категорий
    products = Product.objects.all()  # Получение всех продуктов

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'catalog/catalog_items.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, 'catalog/product_detail.html', {'product': product})
