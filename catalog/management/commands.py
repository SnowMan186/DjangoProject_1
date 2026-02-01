from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.serializers import deserialize

class Command(BaseCommand):
    help = 'Clear all product/category data and load test data.'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('fixtures/data.json') as file:
            deserialized_objects = deserialize("json", file.read())
            for obj in deserialized_objects:
                obj.save()
