from django.urls import path
from .views import HomePageView, MusicanListView, MusicanDetailView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),  # Home page for podcasts
    path('musican/', MusicanListView.as_view(), name="musican_list"),  # Musician list page
    path('musican/<int:pk>/', MusicanDetailView.as_view(), name='musican_detail'),  # Musician detail page
]
