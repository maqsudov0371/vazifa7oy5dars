from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('musican/', MisicanView.as_view(), name="musican"),
    path('musican/<int:pk>/', MusicanDetailView.as_view(), name='musican_detail'),  # pk'ni ishlatayotganingizni tekshirib ko'ring
]
