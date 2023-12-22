import random
from django.db import models
from .board import Board


class StackEventsCardsInBoard(models.Model):
    """Board for all stacks in event stacks."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    # def random_event_card(self):
    #     """Choose randomly one event card for events stack."""

    #     event_deck = EventsDeck.objects.get(name="Events Deck")
    #     random_event_card = random.choice(event_deck)
        
    #     return random_event_card


# class StackEventsCards(StackEventsCardsInBoard):
#     """Presents a stack for events cards."""
    
#     event_card = models.ForeignKey(EventCard, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Stack events cards for board - {self.board}"

#     def save(self, *args, **kwargs):
#             """Override save method to set the event_card field."""
#             if not self.event_card:
#                 self.event_card = self.random_event_card()
#             super().save(*args, **kwargs)


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