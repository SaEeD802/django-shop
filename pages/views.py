from django.shortcuts import render
from django.views import generic


# Create your views here.
class home_page(generic.TemplateView):
    template_name = 'pages/home.html'
