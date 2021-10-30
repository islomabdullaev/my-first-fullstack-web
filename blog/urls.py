from django.urls import path

from blog.views import BlogListView, BlogDetailView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog-page"),
    path("<int:pk>/comment/", CommentCreateView.as_view(), name="comment"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail")
]