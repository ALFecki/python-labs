from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.index, name="home"),
    path("categories", views.category_list, name="categories"),
    path("create-category", views.create_category, name="create_category"),
    path("create-model", views.create_model, name="create_model"),
    path("about", views.about_us, name="about"),
    path("news", views.news, name="news"),
    path("contacts", views.contacts, name="contacts"),
    path("toys-list/create", views.create_product, name="create"),
    path("toys-list/delete/<int:id>", views.delete_product, name="delete"),
    path("toys-list/edit/<int:id>", views.edit_product, name="edit"),
    path("toys-list/detail/<int:id>", views.product_details, name="detail"),
    path("toys-list/<str:category>", views.toys_list, name="toys_list_by_category"),
    path("toys-list", views.toys_list, name="toys_list"),
]
