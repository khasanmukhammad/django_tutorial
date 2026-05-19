from django.urls import path
from .views import HomeView, MessageView

urlpatterns = [
    path('', HomeView, name='home'),
    path('message/', MessageView, name='message'),
]