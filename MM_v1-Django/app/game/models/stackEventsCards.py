from django.db import models
from .game import Game
from dataset.models import EventCard


class StackEventsCards(models.Model):
    """Presents a stack for events cards in board"""
    
    game_number = models.ForeignKey(Game, on_delete=models.CASCADE, default=100, null=True, blank=True)
    game_round = models.IntegerField(default=0)
    event_card = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Stack events card."

















# class StackNPCDutchCaptains(StackEventsCardsInBoard):
#     """Presents a stack NPC Dutch Captains cards on board."""

#     npc_dutch_captain = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC dutch captains cards for board - {self.board}"


# class StackNPCEnglishCaptains(StackEventsCardsInBoard):
#     """Presents a stack NPC English Captains cards on board."""

#     npc_english_captain = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC english captains cards for board - {self.board}"


# class StackNPCFrenchCaptains(StackEventsCardsInBoard):
#     """Presents a stack NPC French Captains cards on board."""

#     npc_french_captain = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC french captains cards for board - {self.board}"


# class StackNPCSpanishCaptains(StackEventsCardsInBoard):
#     """Presents a stack NPC Spanish Captains cards on board."""

#     npc_spanish_captain = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC spanish captains cards for board - {self.board}"


# class StackNPCSloopPirate(StackEventsCardsInBoard):
#     """Presents a stack NPC Sloop Pirate cards on board."""

#     npc_sloop_pirate = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC sloop pirate cards for board - {self.board}"


# class StackNPCFrigatePirate(StackEventsCardsInBoard):
#     """Presents a stack NPC Frigate Pirate cards on board."""

#     npc_frigate_pirate = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack NPC frigate pirate cards for board - {self.board}"







    # def save(self, *args, **kwargs):
    #     # If card_event is not already assigned, assign a random event card
    #     if not self.card_event:
    #         self.random_event_card()

    #     super().save(*args, **kwargs)