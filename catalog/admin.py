from django.contrib import admin

from catalog.models import Category, Product


from django.contrib import admin
from .models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price',
                    'category', 'user', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name', 'description', 'user__username')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_version',
                    'name', 'current_version')
    list_filter = ('product__name', 'current_version')
    search_fields = ('name', 'product__name')
