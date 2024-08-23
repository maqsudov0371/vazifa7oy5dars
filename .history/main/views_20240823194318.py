from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView

class HomePageView(ListView):
    model = Podca
    template_name = 'index.html'
    context_object_name = 'podca'

class MisicanView(ListView):
    model = Musican
    template_name = 'musican.html'
    context_object_name = 'musican'

class MusicanDetailView(DetailView):
    model = Musican
    template_name = 'musican_detail.html'
    context_object_name = 'musican'
