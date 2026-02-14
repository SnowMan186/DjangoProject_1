from django.views.generic import TemplateView, DetailView, ListView
from .models import Product

class HomeView(TemplateView):
    template_name = 'home.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
