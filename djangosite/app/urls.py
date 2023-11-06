# BEGIN: 5f3d8a1d8c5a
from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]