from django.db import models
from django.utils.translation import gettext as _


class ContactModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_("name"))
    email = models.EmailField(max_length=50, verbose_name=_("email"))
    phone = models.CharField(max_length=12, verbose_name=_("phone"))
    message = models.TextField(verbose_name=_("message"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class AboutUsModel(models.Model):
    about_email = models.EmailField(max_length=50, verbose_name=_("about_email"))
    about_message = models.TextField(verbose_name=_("about_message"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.about_email

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"


