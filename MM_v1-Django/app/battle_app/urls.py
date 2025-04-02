from django.urls import path
from . import views

app_name = 'battle_app'

urlpatterns = [
    path('battleApp', views.battleApp, name='battle_app'),
    path('combatFlow', views.combatFlow, name='combatFlow'),
    path('combatFlowDiagram', views.combatFlowDiagram, name='combatFlowDiagram'),
    path('dices', views.dices, name='dices'),
    path('round', views.round, name='round'),
    path('seaBattle', views.seaBattle, name='seaBattle'),
]
