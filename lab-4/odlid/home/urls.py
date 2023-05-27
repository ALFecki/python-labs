from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home')
]