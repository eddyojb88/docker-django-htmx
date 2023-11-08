# BEGIN: 5f3d8a1d8c5a
from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('getlinechart', views.getlinechart, name='getlinechart'),
    path('echarts', views.dashboard_view, name='echarts-dashboard'),
    path('charts', views.chart_view_hx, name='charts-hx')
]
