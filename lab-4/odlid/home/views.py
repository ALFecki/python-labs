from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product, ProductModel
from django.core.exceptions import PermissionDenied
from .forms import ProductForm
from django.http import HttpResponseRedirect, HttpResponseNotFound


def category_list(request, category=None):
    categories = ProductCategory.objects.all()

    return render(request, "categories.html", {"categories": categories})


def toys_list(request, category=None):
    categories = ProductCategory.objects.all()
    if category:
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


def product_details(request, id):

    product = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'product':product})




def create_product(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    form = ProductForm()

    if request.method == "POST":
        product = Product.objects.create(
            name=request.POST.get("name"),
            code=request.POST.get("code"),
            model=ProductModel.objects.get(id=request.POST.get("model")),
            cost=request.POST.get("cost"),
            in_prod=request.POST.get("in_prod") == "on",
            category=ProductCategory.objects.get(id=request.POST.get("category")),
        )
        product.save()
    else:
        return render(request, "create.html", {"form": form})
    return HttpResponseRedirect("/")


def edit_product(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is to weak")

    
    try:
        product = Product.objects.get(id=id)
        
        form = ProductForm(initial= 
            {
                "name": product.name,
                "code": product.code,
                "model": product.model,
                "cost": product.cost,
                "in_prod": product.in_prod,
                "category": product.category,
            }
        )

        if request.method == "POST":
            product.name = request.POST.get('name')
            product.code = request.POST.get('code')
            product.model = ProductModel.objects.get(id=request.POST.get('model'))
            product.cost = request.POST.get('cost')
            product.in_prod = request.POST.get('in_prod') == 'on'
            product.category = ProductCategory.objects.get(id=request.POST.get('category'))

            product.save()

            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'product':product, 'form':form})
    except:
        return HttpResponseNotFound('<h2>Product is not found</h2>')
