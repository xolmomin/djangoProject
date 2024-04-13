from django.urls import path

from apps.views import MainMenuListView

urlpatterns = [
    path('', MainMenuListView.as_view())
]
