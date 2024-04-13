from django.views.generic import ListView

from apps.models import Product


class MainMenuListView(ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
    context_object_name = 'products'
