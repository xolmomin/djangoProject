from django.views.generic import ListView
from rest_framework.generics import ListAPIView

from apps.models import Product
from apps.serializers import ProductTranslatableModelSerializer


class MainMenuListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductTranslatableModelSerializer


'''
n + 1 problem

'''