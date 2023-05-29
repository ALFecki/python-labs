from django.shortcuts import render
from .models import ProductCategory, Product, ProductModel
from django.core.exceptions import PermissionDenied
from .forms import ProductForm
from django.http import HttpResponseRedirect


def category_list(request, category=None):
    categories = ProductCategory.objects.all()

    return render(request, "categories.html", {"categories": categories})


def toys_list(request, category=None):
    categories = ProductCategory.objects.all()
    if (category):
        toys = Product.objects.filter(category=category)
        category = ProductCategory.objects.get(id=category).name
    else:
        toys = Product.objects.all()
    
    
    print(category)
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


def create_product(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")
    
    form = ProductForm()

    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code'),
            model = ProductModel.objects.get(id=request.POST.get('model')),
            cost = request.POST.get('cost'),
            in_prod = request.POST.get('in_prod') == "on" ,
            category= ProductCategory.objects.get(id=request.POST.get('category'))
        )
        product.save()
    else:
        return render(request, "create.html", {"form" : form})
    return HttpResponseRedirect('/')
