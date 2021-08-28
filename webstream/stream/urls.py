from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='stream-home'),
    path('about/', views.about, name='stream-about'),
    path('mystream', views.mystream, name='stream-mystream'),
    path("start_stream", views.start_stream, name="start-stream"),
 ]
