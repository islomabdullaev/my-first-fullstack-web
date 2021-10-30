from django.db import models
from django.utils.translation import gettext as _


class AuthorModel(models.Model):
    full_name = models.CharField(max_length=54, verbose_name=_("full name"))
    avatar = models.ImageField(upload_to="media/blog/avatars", verbose_name=_("avatar"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    image = models.ImageField(upload_to="media/blog", verbose_name=_("image"))
    author = models.ForeignKey(AuthorModel, related_name="posts", on_delete=models.PROTECT, verbose_name=_("author"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")


class PostCommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name="comments", on_delete=models.CASCADE, verbose_name=_("post"))

    name = models.CharField(max_length=32, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    phone = models.CharField(max_length=13)
    comment = models.TextField(verbose_name=_("comment"))

    created_at = models.DateTimeField(auto_now_add=True, null=True)


