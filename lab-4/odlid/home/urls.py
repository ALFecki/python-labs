from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.category_list, name="home"),
    path("toys_list", views.toys_list, name="toys_list"),
    path("toys_list/<str:category>", views.toys_list, name="toys_list_by_category"),
    path("create", views.create_product, name="create")
]
