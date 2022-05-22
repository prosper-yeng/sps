from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import Permission, User
from django.utils.timezone import now

Permission.add_to_class('status', models.CharField(max_length=180, choices=StatusChoice.choices, default=StatusChoice.CREATED))
Permission.add_to_class('created_by', models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='permission_created_by'))
Permission.add_to_class('created_on',  models.DateTimeField( default=now))
