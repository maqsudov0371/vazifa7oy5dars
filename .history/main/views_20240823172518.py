from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Course, User, Contact
from django.contrib.messages import warning, success
from .utils import send_verification_email
from django.contrib.auth import authenticate, login
from django.views.generic import ListView

class HomePageView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'
    paginate_by = 3