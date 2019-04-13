from django.urls import path
from . import views

urlpatterns = [
    # '' represents the root of the app
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),  # added
    path('greet/', views.greet, name='greet'),  # added
]
