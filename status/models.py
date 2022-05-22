from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from choice.views import StatusChoice


# Create your models here.
class Status ( models.Model ):
    name = models.CharField ( max_length=100, null=False, unique=True )
    created_by = models.ForeignKey ( User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='status_created_by' )
    created_on = models.DateTimeField ( default=now )

    def __str__(self):
        return self.name
