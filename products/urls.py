from django.urls import path

from products.views import ProductTemplateView, ProductDetailView, update_wishlist, WishlistView, update_cart, \
    CartListView

app_name = "products"

urlpatterns = [
    path("", ProductTemplateView.as_view(), name="page"),
    path("wishlist/", WishlistView.as_view(), name="wishlist"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("<int:pk>/cart/", update_cart, name="update-cart"),
    path("<int:pk>/wishlist", update_wishlist, name="update-wishlist"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
