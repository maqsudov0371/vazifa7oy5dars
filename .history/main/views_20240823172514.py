from django.shortcuts import render, redirect


class HomePageView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'
    paginate_by = 3