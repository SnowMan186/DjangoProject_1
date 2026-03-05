from django.core.management.base import BaseCommand
from catalog.models import Product
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Creates groups and permissions'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Product)
        permission = Permission.objects.create(
            codename='can_unpublish_product',
            name='Может снимать продукт с публикации',
            content_type=content_type
        )

        group_moderators = Group.objects.create(name='Модераторы продуктов')
        group_moderators.permissions.add(permission)
        group_moderators.permissions.add(Permission.objects.get(codename='delete_product'))


