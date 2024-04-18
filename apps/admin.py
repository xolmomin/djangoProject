from django.contrib import admin
from apps.models import Product, Category, TgUser

from parler.admin import TranslatableAdmin


@admin.register(TgUser)
class TgUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']


@admin.register(Product)
class ProductModelAdmin(TranslatableAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
