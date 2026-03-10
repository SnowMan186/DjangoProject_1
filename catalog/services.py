from django.core.cache import cache
from catalog.models import Product, Category

def get_products_in_category(category_slug):
    cached_result = cache.get(f'products_{category_slug}')
        return cached_result

    try:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        cache.set(f'products_{category_slug}', products, timeout=60 * 15)
    except Category.DoesNotExist:
        return []