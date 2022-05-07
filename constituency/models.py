from django.db import models
from choice.views import StatusChoice,DistrictChoice
from district.models import District
from region.models import Region


# Create your models here.
class Constituency (models.Model):
    region=models.ForeignKey('region.Region', on_delete=models.CASCADE, related_name='region')
    name_of_constituency = models.CharField ( max_length=100, null=False, unique=True )
    constituency_code = models.CharField ( max_length=50, null=False, unique=True )
    district = models.ForeignKey ( District, on_delete=models.CASCADE, related_name='district' )

    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_constituency
