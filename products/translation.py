from modeltranslation.translator import register, TranslationOptions

from products.models import ProductModel, CategoryModel, ColorModel, ProductTagModel


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "long_description")


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ProductTagModel)
class TagTranslationOptions(TranslationOptions):
    fields = ("title",)

