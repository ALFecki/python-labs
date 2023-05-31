from django.urls import path
import views


app_name = 'account'

urlpatterns = [
    path('history', views.user_order_history, name='history')
]