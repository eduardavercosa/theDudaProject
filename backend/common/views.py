from django.views.generic import TemplateView


class Home_View(TemplateView):
    template_name = "index.html"
