from django.db import models
from choice.views import StatusChoice
from constituency.models import Constituency


# Create your models here.
class ElectoralArea (models.Model):
    constituency=models.ForeignKey(Constituency, on_delete=models.CASCADE, related_name='electoral_area_const')
    name_of_electoral_area = models.CharField ( max_length=100, null=False, unique=True )
    electoral_area_code = models.CharField ( max_length=50, null=False, unique=True )
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_constituency
