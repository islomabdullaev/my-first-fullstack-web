from django.urls import path

from accounts.views import SignUpView, ProfileTemplateView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileTemplateView.as_view(), name="profile"),
]
