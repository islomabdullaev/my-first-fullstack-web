from django.views.generic import TemplateView


class BlogTemplateView(TemplateView):
    template_name = "blog.html"
