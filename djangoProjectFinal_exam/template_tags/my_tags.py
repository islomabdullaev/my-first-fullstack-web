from django import template

from products.models import WishlistModel

register = template.Library()


@register.filter
def in_wishlist(product, user):
    return WishlistModel.objects.filter(user=user, product=product).exists()


