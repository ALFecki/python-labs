from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from order.models import Order



def user_order_history(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be authorized")
    

    orders = Order.objects.filter(client_id=request.user.id)

    return render(request, 'history.html', {'orders':orders})