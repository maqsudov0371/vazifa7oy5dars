from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView

class HomePageView(ListView):
    model = Podca
    template_name = 'index.html'
    context_object_name = 'courses'