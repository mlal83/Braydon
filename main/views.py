from django.shortcuts import render
from django.views.generic import ListView
from .models import About


class AboutList(ListView):
    """
    Renders a list of About pages
    """
    queryset = About.objects.all()
    model = About  # Specify the model to work with
    template_name = "about/about.html"  # Specify the template to render
    context_object_name = "about_pages"  # Specify the context object name to use in the template
    #html_content = model.mydiary