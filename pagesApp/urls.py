from django.urls import path, include
from . import views


urlpatterns = [
    path('test', views.test, name="test"),
    path('home', views.home, name="home"),
    path('email', views.sendgridtest, name="sendgridtest"),
    path('approve/<slug:slug_text>', views.approve, name="approve"),
    path('edit/<slug:slug_text>', views.editProfile_Ex, name="editProfile_Ex"),
    path('expert/<slug:slug_text>', views.expertProfile, name="expertProfile"),
    ]