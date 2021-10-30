from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import ProductModel, CategoryModel, ColorModel, PriceFilterModel, ProductTagModel


@admin.register(ProductModel)
class ProductModelAdmin(TranslationAdmin):
    list_display_links = ["created_at"]
    list_display = ["title", "price", "created_at"]
    list_filter = ["title", "created_at"]
    search_fields = ["title"]


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ["title", "created_at"]


@admin.register(ColorModel)
class ColorModelAdmin(TranslationAdmin):
    list_display_links = ["created_at"]
    list_display = ["title", "created_at"]


@admin.register(ProductTagModel)
class ProductTagModelAdmin(TranslationAdmin):
    list_display_links = ["created_at"]
    list_display = ["title", "created_at"]
    list_filter = ["title"]


@admin.register(PriceFilterModel)
class PriceFilterModelAdmin(admin.ModelAdmin):
    list_display = ["min", "max"]
