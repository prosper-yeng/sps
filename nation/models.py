from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice


# Create your models here.
class Nation (models.Model):
    name_of_nation = models.CharField ( max_length=100, null=False,unique=True)
    status = models.ForeignKey ( 'status.Status', on_delete=models.CASCADE, related_name='nation_status' )
    created_on = models.DateTimeField ( default=now )

    def __str__(self):
        return self.name_of_nation
