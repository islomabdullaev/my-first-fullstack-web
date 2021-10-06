from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"


class AboutTemplateView(TemplateView):
    template_name = "about.html"


class BlogTemplateView(TemplateView):
    template_name = "blog.html"


class ProductsTemplateView(TemplateView):
    template_name = "products.html"


class WishlistView(TemplateView):
    template_name = "wishlist.html"


# class ProductDetailView(DetailView):