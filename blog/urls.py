from django.urls import path
from . import views
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('list/', views.BlogListView.as_view(), name='list'),
    path('view/<int:pk>', views.BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>', views.BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>', views.toggle_activity, name='toggle_activity'),
]