from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView

class HomePageView(ListView):
    model = Podca
    template_name = 'index.html'
    context_object_name = 'podca'


class MisicanView(ListView):
    model = Musican
    template_name = 'musican.html'
    context_object_name = 'musican'


class PodcaDetailView(DetailView):
    model = Podca
    template_name = 'podca_detail.html'
    context_object_name = 'podca'