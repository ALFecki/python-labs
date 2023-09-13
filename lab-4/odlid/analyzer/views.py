from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from order.models import Order, OrderItem
from analyzer.models import Review, PromoCode
from home.models import Product
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from io import BytesIO
import base64
import matplotlib.pyplot as plt


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


def get_plot():
    x = [o.created for o in Order.objects.all()]
    y = []
    for el in x:
        orders_in_date = Order.objects.all().filter(created=el)
        for order in orders_in_date:
            quantity = sum([i.quantity for i in order.items.all()])
        y.append(quantity)

    plt.plot(x, y)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode("utf-8")


def shop_analyzer(request):
    if not request.user.is_staff:
        raise PermissionDenied("Your role is too weak")

    purchase_count = Product.objects.values_list("cost", "purchase_count")

    total_income = 0
    total_count = 0

    for el in purchase_count:
        total_income += el[0] * el[1]
        total_count += el[1]

    most_valuable_product = Product.objects.order_by("purchase_count").first()
    min_valuable_product = Product.objects.order_by("-purchase_count").first()
    plot = get_plot()
    return render(
        request,
        "analyze.html",
        {
            "total_income": total_income,
            "total_count": total_count,
            "most_valuable_product": most_valuable_product,
            "min_valuable_product": min_valuable_product,
            "plot": plot,
        },
    )


def reviews_page(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})


def create_review(request):
    if request.method == "POST":
        review = Review(
            user=request.user,
            date=datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
            rating=request.POST.get("rating"),
            description=request.POST.get("description"),
        )
        review.save()
    else:
        return render(request, "create_review.html")

    return HttpResponseRedirect("/account/reviews")


def promo(request):
    promo_codes = PromoCode.objects.all()
    return render(request, "promo.html", {"promocodes": promo_codes})
