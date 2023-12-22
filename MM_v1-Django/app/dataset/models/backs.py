from django.db import models


class Back(models.Model):
    """Back image for tokens, cards and other elements in game."""

    name = models.CharField(max_length=50)
    rewers = models.ImageField(upload_to='backs/', blank=True, null=True)

    # def __str__(self):
    #     return f"Back for - {self.name}"
    def __str__(self):
        return self.rewers.url
