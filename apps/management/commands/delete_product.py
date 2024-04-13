import os.path

from django.core.management.base import BaseCommand, CommandError
from apps.models import Product, ProductImage
from djangoProject.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = "Change product activate fields"

    def handle(self, *args, **options):
        media_paths = list(map(lambda i: i.split('/')[-1], ProductImage.objects.values_list('image', flat=True)))
        location = os.path.join(MEDIA_ROOT, 'products')
        for item in os.listdir(location):
            if item not in media_paths:
                os.remove(os.path.join(location, item))
        self.stdout.write(self.style.SUCCESS('Successfully change product activate fields'))
