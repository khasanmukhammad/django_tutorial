from django.urls import path
from .views import HomePageView, AboutPageView, NewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('news/', NewsPageView.as_view(), name = 'news' ),
]