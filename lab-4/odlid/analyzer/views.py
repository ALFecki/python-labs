from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from order.models import Order, OrderItem



def user_order_history(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be authorized")
    

    orders = Order.objects.filter(client_id=request.user.id)
    order_items = dict()
    for o in orders:
        order_items[o.id] = OrderItem.objects.filter(order_id=o.id)
    

    return render(request, 'history.html', {'orders':orders, 'order_items': order_items})