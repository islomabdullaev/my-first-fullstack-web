from django.contrib import admin

from blog.models import PostModel, AuthorModel, PostCommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["full_name", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["full_name"]


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(PostCommentModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]

