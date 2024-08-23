from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Podca, Musican

# Home page view for podcasts
class HomePageView(ListView):
    model = Podca
    template_name = 'index.html'
    context_object_name = 'podca'

# Musican list view
class MusicanListView(ListView):
    model = Musican
    template_name = 'musican.html'
    context_object_name = 'musicans'

# Musican detail view
class MusicanDetailView(DetailView):
    model = Musican
    template_name = 'musican_detail.html'
    context_object_name = 'musican'
