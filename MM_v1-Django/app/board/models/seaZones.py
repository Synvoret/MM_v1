from django.db import models
from .board import Board


class SeaZone(models.Model):
    """Base class model for sea zones and coordinates for all components on it."""

    SEAZONES = [
        ('Basse-Terre', 'Basse-Terre'),
        ('Bridgetown', 'Bridgetown'),
        ('Caracas', 'Caracas'),
        ('Cartagena', 'Cartagena'),
        ('Curacao', 'Curacao'),
        ('Gulf City', 'Gulf City'),
        ('Havana', 'Havana'),
        ('Nassau', 'Nassau'),
        ('Old Providence', 'Old Providence'),
        ('Petite Goave', 'Petite Goave'),
        ('Port Royal', 'Port Royal'),
        ('San Juan', 'San Juan'),
        ('Santo Domingo', 'Santo Domingo'),
        ('St John', 'St John'),
        ('St Maarten', 'St Maarten'),
        ('The Carribean Sea', 'The Carribean Sea'),
        ('Tortuga', 'Tortuga'),
        ('Trinidad', 'Trinidad'),
    ]

    class Meta:
        verbose_name = "Sea Zone"

    # board = models.ForeignKey(Board, on_delete=models.CASCADE, default=1)
    sea_zone_name = models.CharField(max_length=50)
    sea_zone_coordinates = models.CharField(max_length=500)
    n_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    ne_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    e_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    se_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    s_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    sw_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    w_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    nw_direction = models.CharField(max_length=50, null=True, blank=True, choices=SEAZONES)
    name_cx = models.IntegerField()
    name_cy = models.IntegerField()
    name_rx = models.IntegerField()
    name_ry = models.IntegerField(null=True, blank=True)
    name_rotate = models.IntegerField()
    feature_coordinates = models.CharField(max_length=500)
    demand_x = models.IntegerField()
    demand_y = models.IntegerField()
    demand_rotate = models.IntegerField()
    mission_sign_x = models.IntegerField(null=True, blank=True)
    mission_sign_y = models.IntegerField(null=True, blank=True)
    modification_x = models.IntegerField()
    modification_y = models.IntegerField()
    modification_rotate = models.IntegerField()
    nationality_x = models.IntegerField()
    nationality_y = models.IntegerField()
    nationality_rotate = models.IntegerField()
    merchant_x = models.IntegerField()
    merchant_y = models.IntegerField()
    location_x = models.IntegerField()
    location_y = models.IntegerField()

    def __str__(self):
        return f"Sea Zone - {self.sea_zone_name}"
