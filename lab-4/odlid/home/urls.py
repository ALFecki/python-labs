from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.category_list, name="home"),
    path("toys_list/create", views.create_product, name="create"),
    path("toys_list/delete/<int:id>", views.delete_product, name="delete"),
    path("toys_list/<str:category>", views.toys_list, name="toys_list_by_category"),
    path("toys_list/detail/<int:id>", views.product_details, name="detail"),
    path("toys_list/edit/<int:id>", views.edit_product, name="edit"),
    path("toys_list", views.toys_list, name="toys_list"),
]
