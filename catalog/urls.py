from django.urls import include, path

from . import views
from .views import ContactsView, CatalogItemsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, AddVersionView

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogItemsView.as_view(), name='catalog_items'),
    path('product/<int:product_id>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('product/', include([
        path('product/create/', ProductCreateView.as_view(),
             name='create_product'),

        path('update/<int:pk>/', ProductUpdateView.as_view(),
             name='product_update'),

        path('delete/<int:pk>/', ProductDeleteView.as_view(),
             name='product_delete'),

        path('product/list/', ProductListView.as_view(), name='product_list'),
        path('add_version/<int:product_id>/',
             views.AddVersionView.as_view(), name='add_version'),
    ])),
]
