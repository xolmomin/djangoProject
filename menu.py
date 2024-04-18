import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
import django

django.setup()
from apps.models import Product

while True:
    menu = '''
    1. Product lar listini chiqarish
    2. Product ochirish (id)
    3. exit
    '''

    key = input(menu)
    if key == '1':
        langauges = ('en', 'uz', 'ko')
        lang = input(f'Tilni kiriting {langauges}: ')
        while lang not in langauges:
            lang = input(f'Tilni kiriting {langauges}: ')
        queryset = Product.objects.translated(lang)
        print('Productlar soni :', queryset.count())
        for product in queryset:
            print(product.id, product.name, product.price, (product.category.id, product.category.name))

    elif key == '2':
        _id = input('id ni kiriting!')
        Product.objects.filter(id=_id).delete()
    elif key == '3':
        exit()
