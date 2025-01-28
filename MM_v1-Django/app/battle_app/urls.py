from django.urls import path
from . import views

app_name = 'battle_app'

urlpatterns = [
    path('battleApp', views.battleApp, name='battle_app'),
    path('combatFlowDiagram', views.combatFlowDiagram, name='combatFlowDiagram'),
    path('playerAttackNPC', views.playerAttackNPC, name='playerAttackNPC'),
]
