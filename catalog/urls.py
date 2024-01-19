from django.urls import include, path

from . import views
from .views import ContactsView, CatalogItemsView, ProductDetailView

app_name = 'catalog'  # Пространство имён для приложения "catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('catalog/', views.CatalogItemsView.as_view(), name='catalog_items'),
    path('product/<int:product_id>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('product/', include([
        path('product/create/', views.product_create, name='create_product'),

        path('update/<int:pk>/', views.product_update, name='update'),
        path('delete/<int:pk>/', views.product_delete, name='delete'),
        path('product/list/', views.product_list, name='product_list'),
    ])),
]
