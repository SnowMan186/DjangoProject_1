from django.urls import path
from .views import home_view, contacts_view
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('contacts/', contacts_view, name='contacts'),
]

app_name = 'catalog'

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail'),
]