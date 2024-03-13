from django.urls import path
from . import views

app_name = 'nav'

urlpatterns = [
    path('navStartPlayerActions', views.navStartPlayerActions, name='navStartPlayerActions'),
    path('navMoveActions', views.navMoveActions, name='navMoveActions'),
    path('navScoutActions', views.navScoutActions, name='navScoutActions'),
    path('navPortActions', views.navPortActions, name='navPortActions'),
    path('navLocationActions', views.navLocationActions, name='navLocationActions'),
    path('resetNav', views.resetNav, name="resetNav"),
]
