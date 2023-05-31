from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied
from .cart import Cart
from .forms import CartAddProductForm
from home.models import Product


@require_POST
def cart_add(request, product_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must to sign in")

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must to sign in")

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must to sign in")
    cart = Cart(request)
    return render(request, 'cart/details.html', {'cart': cart})