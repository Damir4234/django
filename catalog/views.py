
from catalog.forms import EditProductForm, ModeratorProductForm, ProductForm, VersionForm
from catalog.models import Category, Product
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Category, Product, Version
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(View):
    def get(self, request):
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
    template_name = 'catalog/product_detail.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        versions = product.versions.all()

        return render(request, self.template_name, {'product': product, 'versions': versions})


@method_decorator(login_required, name='dispatch')
class ProductCreateView(View):
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()

            version_name = form.cleaned_data.get('version_name')
            version_number = form.cleaned_data.get('version_number')

            if version_name and version_number:
                version = Version.objects.create(
                    product=product,
                    name=version_name,
                    number_version=version_number,
                    current_version=True
                )

            return redirect('catalog:product_list')

    def get(self, request):
        form = ProductForm()
        return render(request, 'catalog/product_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_detail', product_id=product.pk)

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = EditProductForm(instance=product)
        return render(request, 'catalog/product_form.html', {'form': form, 'product': product})


class ProductDeleteView(View):
    def post(self, request, pk):
        Product.objects.get(pk=pk).delete()
        return redirect('product:list')


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'catalog/product_list.html', {'products': products})


class AddVersionView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        version_form = VersionForm(request.POST)
        if version_form.is_valid():
            version = version_form.save(commit=False)
            version.product = product
            version.save()
            return redirect('product_detail', product_id=product.id)

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        version_form = VersionForm()
        return render(request, 'add_version.html', {'version_form': version_form, 'product': product})
