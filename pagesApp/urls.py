from django.urls import path, include
from . import views


urlpatterns = [
    path('landingpage', views.index, name="index"),
    path('home', views.home, name="home"),
    ]