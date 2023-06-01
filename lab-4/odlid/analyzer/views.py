from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from order.models import Order, OrderItem
from home.models import Product
from functools import reduce


def user_order_history(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be authorized")

    orders = Order.objects.filter(client_id=request.user.id)
    order_items = dict()
    for o in orders:
        order_items[o.id] = OrderItem.objects.filter(order_id=o.id)

    return render(
        request, "history.html", {"orders": orders, "order_items": order_items}
    )


def shop_analyzer(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is too weak")

    products = Product.objects.all()
    purchase_count = Product.objects.values_list("cost", "purchase_count")

    print(purchase_count[0][1])
    print(purchase_count)
    max_purchases = reduce(lambda x, y: x if x[1] > y[1] else y, purchase_count)
    min_purchases = reduce(lambda x, y: x if x[1] < y[1] else y, purchase_count)
    
    total_income = 0
    total_count = 0
    
    for el in purchase_count:
        total_income += el[0] * el[1]
        total_count += el[1]

    most_valuable_product = Product.objects.order_by('purchase_count').first()
    min_valuable_product = Product.objects.order_by('-purchase_count').first()

    return render(
        request,
        "analyze.html",
        {
            "total_income": total_income,
            "total_count": total_count,
            "most_valuable_product": most_valuable_product,
            "min_valuable_product": min_valuable_product,
        },
    )
