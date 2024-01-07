from django.urls import path

from . import views
from .views import ContactsView, CatalogItemsView, ProductDetailView

urlpatterns = [
    path('', views.index, name='index'),  # URL для главной страницы
    path('contacts/', ContactsView.as_view(), name='contacts'),  # URL для страницы контактов
    path('catalog/', CatalogItemsView.as_view(), name='catalog_items'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail')
]