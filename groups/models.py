from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import Group, User

Group.add_to_class('status', models.CharField(max_length=180, choices=StatusChoice.choices, default=StatusChoice.CREATED))
Group.add_to_class('created_by', models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='group_created_by'))
