from django.urls import path
from .views import ThreeNewsList

urlpatterns = [
  path('', ThreeNewsList.as_view(), name='news-list')
]
