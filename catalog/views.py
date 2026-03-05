from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render


class HomeView(TemplateView):
    template_name = 'home.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = '/'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    success_url = '/products/'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = '/products/'


@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.publication_status = 'draft'
    product.save()
    return redirect('product_list')


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})



@user_passes_test(lambda u: u.groups.filter(name='Модераторы продуктов').exists() or u == Product.owner)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')
