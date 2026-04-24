from zipfile import Path

from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name = 'home'),
]