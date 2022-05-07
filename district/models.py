from django.db import models
from choice.views import StatusChoice
from region.models import Region


# Create your models here.
class District (models.Model):
    region=models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district')
    name_of_district = models.CharField ( max_length=100, null=False,unique=True)
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_district
