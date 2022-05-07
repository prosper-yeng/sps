from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User, Group
from service_type.models import ServiceType


class GroupService(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    class Meta:
        unique_together =('service_type', 'group')

    def __str__(self):
        return '{} - {}'.format(self.group, self.service_type)
