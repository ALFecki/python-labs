from django.shortcuts import render, get_object_or_404
from django import views
from .models import ProductCategory, Product, ProductModel
from django.core.exceptions import PermissionDenied
from .forms import ProductForm, ProductCategoryForm, ProductModelForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic.edit import FormView
from cart.forms import CartAddProductForm


def category_list(request, category=None):
    categories = ProductCategory.objects.all()

    return render(request, "categories.html", {"categories": categories})


def toys_list(request, category=None):
    categories = ProductCategory.objects.all()
    print(category)
    if category:
        category = ProductCategory.objects.get(id=category)
        toys = Product.objects.filter(category=category)
    else:
        toys = Product.objects.all()

    sort = request.GET.get('sort')

    if (str(sort) == 'ascending'):
            toys = toys.order_by('cost')
    elif (str(sort) == 'descending'):
        toys = toys.order_by('-cost')
    return render(
        request,
        "toys.html",
        {
            "toys": toys,
            "categories": categories,
            "request": request,
            "category": category,

        },
    )


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()


    return render(request, "details.html", {"product": product,"cart_product_form": cart_product_form})


def create_product(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    form = ProductForm()

    if request.method == "POST":
        product = Product.objects.create(
            name=request.POST.get("name"),
            code=request.POST.get("code"),
            image=request.FILES.get("image"),
            model=ProductModel.objects.get(id=request.POST.get("model")),
            cost=request.POST.get("cost"),
            in_prod=request.POST.get("in_prod") == "on",
            category=ProductCategory.objects.get(id=request.POST.get("category")),
        )
        product.save()
    else:
        return render(request, "create.html", {"form": form, 'is_product': True})
    return HttpResponseRedirect("/home")


def edit_product(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    try:
        product = Product.objects.get(id=id)
        
        form = ProductForm(
            initial={
                "name": product.name,
                "code": product.code,
                "model": product.model,
                "image": product.image,
                "cost": product.cost,
                "in_prod": product.in_prod,
                "category": product.category,
            }
        )
        print(request.FILES.get("image"))
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.code = request.POST.get("code")
            product.model = ProductModel.objects.get(id=request.POST.get("model"))
            product.cost = request.POST.get("cost")
            product.image = request.FILES.get("image")
            product.in_prod = request.POST.get("in_prod") == "on"
            product.category = ProductCategory.objects.get(
                id=request.POST.get("category")
            )

            product.save()

            return HttpResponseRedirect("/home/toys-list")
        else:
            return render(request, "edit.html", {"product": product, "form": form, 'is_product': True})
    except:
        return HttpResponseNotFound("<h2>Product is not found</h2>")


def delete_product(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/home/toys-list")
    except:
        return HttpResponseNotFound("<h1>Product not found</h1>")


def create_category(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    form = ProductCategoryForm()

    if request.method == "POST":
        product_category = ProductCategory.objects.create(
            name=request.POST.get("name"), image=request.FILES.get("image")
        )
        product_category.save()
    else:
        return render(request, "create.html", {"form": form})
    return HttpResponseRedirect("/home")


def create_model(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")


    form = ProductModelForm()

    if request.method == "POST":
        product_model = ProductModel.objects.create(
            name=request.POST.get('name'), year_of_manufacture=request.POST.get('year_of_manufacture')
        )
        product_model.save()
    else:
        return render(request, 'create.html', {"form":form})
    return HttpResponseRedirect('/home')