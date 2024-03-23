from django.urls import path
from . import views

app_name = 'nav'

urlpatterns = [
    path('navStartPlayerTurn', views.navStartPlayerTurn, name='navStartPlayerTurn'),
    path('navMoveActions', views.navMoveActions, name='navMoveActions'),
    path('navScoutActions', views.navScoutActions, name='navScoutActions'),
    path('navPortActions', views.navPortActions, name='navPortActions'),
    path('navLocationActions', views.navLocationActions, name='navLocationActions'),
    path('resetNav', views.resetNav, name="resetNav"),
]
