from django.urls import path, include
from .views import HomeView, ContactsView, ProductDetailView, IndexView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('index/', IndexView.as_view(), name='index'),
    path('blogs/', include('blog.urls', namespace='blog')),
]
