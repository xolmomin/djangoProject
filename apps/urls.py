from django.urls import path

from apps.views import MainMenuListView, ProductListAPIView

urlpatterns = [
    path('', MainMenuListView.as_view()),
    path('api/v1/products', ProductListAPIView.as_view())
]
