from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from products.models import ProductModel


class IndexTemplateView(ListView):
    model = ProductModel
    template_name = "home.html"
    context_object_name = "products"