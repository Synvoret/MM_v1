from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('game', views.game, name='game'),
    path('board', views.board, name='board'),
    path('player_board', views.player_board, name='player_board'),
    path('dice', views.dice, name='dice'),
    path('ship', views.ship, name='ship'),

    path('drawEventCard', views.drawEventCard, name='drawEventCard'),
    path('drawMissionCard', views.drawMissionCard, name='drawMissionCard'),
    path('drawGloryCard', views.drawGloryCard, name='drawGloryCard'),
    path('enemyHitLocation', views.enemyHitLocation, name='enemyHitLocation'),
    path('playerCaptainCard', views.playerCaptainCard, name='playerCaptainCard'),
    path('playerShipCard', views.playerShipCard, name='playerShipCard'),
    path('playerHitLocation', views.playerHitLocation, name='playerHitLocation'),
    path('playerGoldsTrack', views.playerGoldsTrack, name='playerGoldsTrack'),
    path('gloryTrackCube', views.gloryTrackCube, name='gloryTrackCube'),
    path('loyalityTrackCube', views.loyalityTrackCube, name='loyalityTrackCube'),
    path('favorsTrackCube', views.favorsTrackCube, name='favorsTrackCube'),

    path('drawDemandToken', views.drawDemandToken, name='drawDemandToken'),
    path('drawMerchantToken', views.drawMerchantToken, name='drawMerchantToken'),
    path('drawShipModification', views.drawShipModification, name='drawShipModification'),
    path('putLocationToken', views.putLocationToken, name='putLocationToken'),
]
