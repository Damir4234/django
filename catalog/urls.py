from django.urls import path

from . import views
from .views import ContactsView, CatalogItemsView, ProductDetailView, product_create, product_delete, product_detail, product_list, product_update

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogItemsView.as_view(), name='catalog_items'),
    path('product/<int:product_id>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('products/', product_list, name='product_list'),
    path('products/new/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]
