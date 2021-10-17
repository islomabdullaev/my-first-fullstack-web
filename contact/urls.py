from django.urls import path

from contact.views import ContactCreateView, AboutUsView

app_name = "contact"

urlpatterns = [
    path("", ContactCreateView.as_view(), name="contact"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
]
