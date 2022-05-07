from django.db import models
from choice.views import StatusChoice


# Create your models here.
class Nation (models.Model):
    name_of_nation = models.CharField ( max_length=100, null=False,unique=True)
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_nation
