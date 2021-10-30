from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import PostModel


class BlogListView(ListView):
    template_name = "blog.html"
    model = PostModel
    context_object_name = "blog_products"

    def get_queryset(self):
        products = PostModel.objects.all()
        return products


class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = "blog_detail.html"
    model = PostModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:detail", kwargs={"pk": self.kwargs.get("pk")})
