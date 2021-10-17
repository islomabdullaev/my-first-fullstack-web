from django.contrib.auth.decorators import login_required
from django.db.models import Min, Max
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView

from products.models import CategoryModel, ColorModel, ProductTagModel, PriceFilterModel, ProductModel, WishlistModel


class ProductTemplateView(ListView):
    paginate_by = 3
    model = ProductModel
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductTemplateView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['categories'] = CategoryModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['prices'] = PriceFilterModel.objects.all()
        context["min_price"] = ProductModel.objects.aggregate(Min("price")).values()
        context["max_price"] = ProductModel.objects.aggregate(Max("price")).values()
        return context

    def get_queryset(self):
        products = ProductModel.objects.order_by("-pk")[:6]
        q = self.request.GET.get("q")
        if q:
            products = ProductModel.objects.filter(title__icontains=q)
        cat = self.request.GET.get("cat")
        if cat:
            products = ProductModel.objects.filter(category_id=cat)
        color = self.request.GET.get("color")
        if color:
            products = ProductModel.objects.filter(color__id=color)
        tag = self.request.GET.get("tag")
        if tag:
            products = ProductModel.objects.filter(tag__id=tag)
        price_filter_min = self.request.GET.get("min")
        price_filter_max = self.request.GET.get("max")
        if price_filter_min and price_filter_max:
            products = ProductModel.objects.aggregate(Min("real_price"), Max("real_price")).values()
        return products


class HomeTemplateView(ListView):
    model = ProductModel
    template_name = "home.html"

    def get_queryset(self):
        products = ProductModel.objects.all()
        return products


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "product-detail.html"
    context_object_name = "product"



# @login_required
# def update_wishlist(request, pk):
#     product = get_object_or_404(ProductModel, pk=pk)
#     WishlistModel.add_or_delete(request.user, product)
#
#     return redirect(request.GET.get("next", "/"))
