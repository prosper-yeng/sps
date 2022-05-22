from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import Group, User
from django.utils.timezone import now

Group.add_to_class('status', models.ForeignKey ('status.Status', on_delete=models.CASCADE, related_name='group_status' ))
Group.add_to_class('created_by', models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='group_created_by'))
Group.add_to_class('created_on',  models.DateTimeField( default=now))
