from django.db import models
from cars.models import Car


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

    car = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,
        related_name="users",
        null=True
    )

    def __str__(self):
        return self.name
