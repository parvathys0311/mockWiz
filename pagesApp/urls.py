from django.urls import path, include
from . import views


urlpatterns = [
    path('test', views.test, name="test"),
    path('home', views.home, name="home"),
    path('email', views.sendgridtest, name="sendgridtest"),
    path('approve/<int:id>', views.approve, name="approve"),
    path('edit/<int:id>', views.editProfile_Ex, name="editProfile_Ex"),
    path('expertProfile', views.expertProfile, name="expertProfile"),
    ]