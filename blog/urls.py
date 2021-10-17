from django.urls import path

from blog.views import BlogTemplateView

app_name = "blog"

urlpatterns = [
    path("", BlogTemplateView.as_view(), name="page")
]