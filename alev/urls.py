from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('alev/<slug>', views.Rem.as_view(), name='rem'),
    path('other/<slug>', views.Other.as_view(), name='other'),
    path('gallery', views.Image.as_view(), name='gallery'),
    path('about', views.About.as_view(), name='about'),
]
