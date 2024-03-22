from django.urls import path
from . import views

#url configuration
urlpatterns = [
    path('homepage/',views.home)
]