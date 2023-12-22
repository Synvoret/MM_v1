from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('game', views.game, name='game'),
    path('board', views.board, name='board'),
    path('drawEventCard', views.drawEventCard, name='drawEventCard'),
    path('drawDemandToken', views.drawDemandToken, name='drawDemandToken'),
    path('drawShipModification', views.drawShipModification, name='drawShipModification'),
    path('drawMerchantToken', views.drawMerchantToken, name='drawMerchantToken'),
    path('gloryTrackCube', views.gloryTrackCube, name='gloryTrackCube'),
    path('enemyHitLocation', views.enemyHitLocation, name='enemyHitLocation'),
    path('putLocationToken', views.putLocationToken, name='putLocationToken'),
]
