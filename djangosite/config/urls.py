"""
URL configuration for djangosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_htmx_examples import views as example_views
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.index),
    path('app/',  include('app.urls')),
    path('example-htmx/',  include('django_htmx_examples.urls')),
    path("example-htmx/", example_views.index, name='django-htmx-index'),
    path("favicon.ico", example_views.favicon),
    path("csrf-demo/", example_views.csrf_demo),
    path("csrf-demo/checker/", example_views.csrf_demo_checker),
    path("error-demo/", example_views.error_demo),
    path("error-demo/trigger/", example_views.error_demo_trigger),
    path("middleware-tester/", example_views.middleware_tester),
    path("middleware-tester/table/", example_views.middleware_tester_table),
    path("partial-rendering/", example_views.partial_rendering),


]
