from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('products/new/', ProductCreateView.as_view(), name='product_new'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
