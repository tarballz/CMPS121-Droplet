from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=20)  # type: str

    # class Meta:
    # 	ordering = ['id']

    def __str__(self):
        return self.name

def save(self, *args, **kwargs):
    options = self.name and {'title': self.title} or {}
    super(Team, self).save(*args, **kwargs)