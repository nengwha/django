from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('whann/', views.whann, name='whann'),
    path('<str:name>', views.greet, name='greet'),
]