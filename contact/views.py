from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from contact.forms import ContactModelForm, AboutUsModelForm
from contact.models import ContactModel


class ContactCreateView(CreateView):
    template_name = "contact.html"
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse("home:page")


class AboutUsView(CreateView):
    template_name = "about.html"
    form_class = AboutUsModelForm

    def get_success_url(self):
        return reverse("home:page")

