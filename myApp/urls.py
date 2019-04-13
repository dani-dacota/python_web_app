from django.urls import path
from . import views

urlpatterns = [
    # '' represents the root of the app
    path('', views.index, name='index'),
]
