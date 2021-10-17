from django.contrib import admin

from products.models import ProductModel, CategoryModel, ColorModel, PriceFilterModel, ProductTagModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "created_at"]
    list_filter = ["title", "created_at"]
    search_fields = ["title"]


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["title"]


@admin.register(PriceFilterModel)
class PriceFilterModelAdmin(admin.ModelAdmin):
    list_display = ["min", "max"]

