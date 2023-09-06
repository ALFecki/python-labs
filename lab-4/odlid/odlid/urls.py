"""
URL configuration for odlid project.

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
from login import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=False), name='index'),
    path("auth/", include('login.urls', namespace="login")),
    path('home/', include('home.urls', namespace='home')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path("admin/", admin.site.urls),
    path('account/', include('analyzer.urls', namespace='account')),
    path('verification/', include('verify_email.urls'))
]