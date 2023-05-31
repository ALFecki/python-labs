from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from cart.cart import Cart
from .models import Order, OrderItem
from login.models import Client

def order_create(request):

    if not request.user.is_authenticated:
        raise PermissionDenied("You must be authorized")

    cart = Cart(request)
    if request.method == 'POST':        
        order = Order.objects.create(client = Client.objects.filter(email=request.user.email).first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            item['product'].purchase_count += item['quantity']
            item['product'].save()
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': order})
    
    return render(request, 'order/create.html',
                  {'cart': cart})