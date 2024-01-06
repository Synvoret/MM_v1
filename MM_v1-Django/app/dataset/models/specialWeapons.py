from django.db import models


class SpecialWeapon(models.Model):
    """Model for special weapons.."""

    class Meta:
        verbose_name = "Special Weapon Token"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='specialWeapons/', blank=True, null=True)

    def __str__(self):
        return f"Special Weapon - {self.name}"
