from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class AboutListView(ListView):
    model = AboutPage
    template_name = 'about_list.html'
    context_object_name = 'about_pages'