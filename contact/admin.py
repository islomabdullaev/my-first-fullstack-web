from django.contrib import admin

from contact.models import ContactModel, AboutUsModel


@admin.register(ContactModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "created_at"]
    list_filter = ["name", "created_at"]


@admin.register(AboutUsModel)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ["about_email", "created_at"]
    list_filter = ["about_email"]

