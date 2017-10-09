from django.db import models
from teams.models import Team


# Create your models here.
class Car(models.Model):
    color_options = (
        (0, 'Red'),
        (1, 'Blue'),
        (2, 'Green'),
        (3, 'Purple'),
    )
    color = models.PositiveSmallIntegerField(choices=color_options)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name="cars",
        null=True
    )

    def __str__(self):
        return self.color_options[self.color][1]
