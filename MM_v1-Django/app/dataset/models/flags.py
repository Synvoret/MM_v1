from django.db import models


class Flag(models.Model):
    """Model for flags tokens."""

    class Meta:
        verbose_name = "Flag"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='flags/', blank=True, null=True)

    def __str__(self):
        return f"Flag - {self.name}"
