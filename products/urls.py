from django.urls import path

from products.views import HomeTemplateView, ContactTemplateView, AboutTemplateView, BlogTemplateView, \
    ProductsTemplateView, WishlistView

app_name = "products"

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("about/", AboutTemplateView.as_view(), name="about"),
    path("blog/", BlogTemplateView.as_view(), name="blog"),
    path("products/", ProductsTemplateView.as_view(), name="products"),
    path("wishlist/", WishlistView.as_view(), name="wishlist"),
    # path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
