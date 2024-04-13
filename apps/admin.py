from django.contrib import admin
from apps.models import Product

from parler.admin import TranslatableAdmin


@admin.register(Product)
class ProductModelAdmin(TranslatableAdmin):
    pass
