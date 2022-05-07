from django.db import models
from choice.views import StatusChoice
from nation.models import Nation


# Create your models here.
class Region (models.Model):
    nation=models.ForeignKey('nation.Nation', on_delete=models.CASCADE, related_name='nation')
    name_of_region = models.CharField ( max_length=100, null=False,unique=True)
    regional_code = models.CharField ( max_length=50, null=False, unique=True )
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )

    def __str__(self):
        return self.name_of_region
