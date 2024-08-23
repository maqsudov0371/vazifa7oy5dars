from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('musican', Musican.as_view(), name="home"),
    ]