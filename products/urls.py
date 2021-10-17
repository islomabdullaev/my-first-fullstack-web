from django.urls import path

from products.views import ProductTemplateView, ProductDetailView

app_name = "products"

urlpatterns = [
    path("", ProductTemplateView.as_view(), name="page"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail")
    # path("<int:pk>/wishlist", update_wishlist, name="update-wishlist"),
]
