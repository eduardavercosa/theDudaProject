from django.views.generic import template_view


class home_view(template_view):
    template_name = "index.html"
