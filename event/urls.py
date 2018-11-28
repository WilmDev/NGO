from django.urls import path
from event import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about', views.about, name='blog-about'),
]
