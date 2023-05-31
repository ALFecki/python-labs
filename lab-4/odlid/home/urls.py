from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.category_list, name="home"),
    path("create-category", views.create_category, name="create_category"),
    path("create-model", views.create_model, name="create_model"),
    path("toys-list/create", views.create_product, name="create"),
    path("toys-list/delete/<int:id>", views.delete_product, name="delete"),
    path("toys-list/<str:category>", views.toys_list, name="toys_list_by_category"),
    path("toys-list/detail/<int:id>", views.product_details, name="detail"),
    path("toys-list/edit/<int:id>", views.edit_product, name="edit"),
    path("toys-list", views.toys_list, name="toys_list"),
]
