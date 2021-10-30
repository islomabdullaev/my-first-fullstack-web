from django.db.models import Sum
from django.template import Library

from products.models import WishlistModel, ProductModel

register = Library()


@register.filter
def in_wishlist(product, user):
    return WishlistModel.objects.filter(user=user, product=product).exists()


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get("cart", [])


@register.simple_tag
def get_cart_info(request):
    cart = request.session.get("cart", [])

    if not cart:
        return 0, 0.0
    return len(cart), ProductModel.get_from_cart(cart).aggregate(Sum("price"))["price__sum"]


