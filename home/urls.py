from django.urls import path

from home.views import IndexTemplateView

app_name = "home"


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="page"),
]
