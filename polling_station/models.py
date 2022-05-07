from django.db import models
from choice.views import StatusChoice
from electoral_area.models import ElectoralArea


# Create your models here.
class PollingStation (models.Model):
    electoral_area=models.ForeignKey(ElectoralArea, on_delete=models.CASCADE, related_name='electoral_area')
    name_of_polling_station = models.CharField ( max_length=100, null=False, unique=True )
    polling_station_code = models.CharField ( max_length=50, null=False, unique=True )
    voters_population = models.IntegerField ()
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_polling_station
