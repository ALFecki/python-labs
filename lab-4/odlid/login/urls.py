from . import views
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name = 'registration'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout')
]