from django.urls import path
from . import views

urlpatterns = [
    path('tomato', views.predictTomatoDisease, name='predictTomatoDisease')
]
