from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('random_number/', views.random_number, name='random_number'),
]
