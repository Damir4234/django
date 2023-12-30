from django.urls import path

from catalog.views import index, contacts

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL для главной страницы
    path('contacts/', views.contacts, name='contacts'),  # URL для страницы контактов
    path('catalog/', views.catalog_items, name='catalog_items'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail')
]
