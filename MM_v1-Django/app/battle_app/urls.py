from django.urls import path
from . import views

app_name = 'battle_app'

urlpatterns = [
    path('battleApp', views.battleApp, name='battle_app'),
    path('combatFlow', views.combatFlow, name='combatFlow'),
    path('combatFlowDiagram', views.combatFlowDiagram, name='combatFlowDiagram'),
    path('declaration', views.declaration, name='declaration'),
    path('dices', views.dices, name='dices'),
    path('seaBattle', views.seaBattle, name='seaBattle'),
    path('seamanship', views.seamanship, name='seamanship'),
    path('shooting', views.shooting, name='shooting'),
    path('statBoard', views.statBoard, name='statBoard'),
]
