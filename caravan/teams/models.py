from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=20)  # type: str

    # class Meta:
    # 	ordering = ['id']

    def __str__(self):
        return self.name
