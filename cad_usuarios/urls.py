from django.urls import path
from app_vitacare import views

urlpatterns = [
    path('', views.home, name='home'),
]
