from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('game', views.game, name='game'),
    path('goGame', views.goGame, name="goGame"),
    path('board', views.board, name='board'),
    path('playerBoard', views.playerBoard, name='playerBoard'),
    path('dice', views.dice, name='dice'),
    path('ship', views.ship, name='ship'),

    path('drawEventCard', views.drawEventCard, name='drawEventCard'),
    path('drawMissionCard', views.drawMissionCard, name='drawMissionCard'),
    path('drawGloryCard', views.drawGloryCard, name='drawGloryCard'),
    path('enemyHitLocation', views.enemyHitLocation, name='enemyHitLocation'),
    path('favorsTrackCube', views.favorsTrackCube, name='favorsTrackCube'),
    path('featuresSeaZones', views.featuresSeaZones, name='featuresSeaZones'),
    path('loyalityTrackCube', views.loyalityTrackCube, name='loyalityTrackCube'),
    path('newPlayer', views.newPlayer, name="newPlayer"),
    path('playerCaptainCard', views.playerCaptainCard, name='playerCaptainCard'),
    path('playerShipCard', views.playerShipCard, name='playerShipCard'),
    path('playerHitLocation', views.playerHitLocation, name='playerHitLocation'),
    path('saveToServerSelectedNewCaptainShip', views.saveToServerSelectedNewCaptainShip, name='saveToServerSelectedNewCaptainShip'),
    path('endCurrentAction', views.playerActions.endCurrentAction, name='endCurrentAction'),
    path('updatePlayerGolds', views.updatePlayerGolds, name='updatePlayerGolds'),
    path('updateGloryTrack', views.updateGloryTrack, name='updateGloryTrack'),

    path('drawDemandToken', views.drawDemandToken, name='drawDemandToken'),
    path('drawMerchantToken', views.drawMerchantToken, name='drawMerchantToken'),
    path('drawShipModification', views.drawShipModification, name='drawShipModification'),
    path('putLocationToken', views.putLocationToken, name='putLocationToken'),

    # player ACTIONs paths
    path('startRound', views.startRound, name='startRound'),
    path('startPlayerActions', views.startPlayerActions, name='startPlayerActions'),
    path('endCurrentAction', views.endCurrentAction, name='endCurrentAction'),
    path('fishingAction', views.fishingAction, name='fishingAction'),
    path('moveAction', views.moveAction, name='moveAction'),
    path('portAction', views.portAction, name='portAction'),
    path('scoutAction', views.scoutAction, name='scoutAction'),
    path('endTurn', views.endTurn, name='endTurn'),
]
