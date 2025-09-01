from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.projects, name='projects'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
]