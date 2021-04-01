from django.views.generic import TemplateView


class MyHomeView(TemplateView):
    template_name = "index.html"
