from django.db import models
from django.contrib.auth.models import User
from choice.views import StatusChoice


class SelectItem(models.Model):
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    parent = models.CharField(max_length=100, null=True)
    parent_name = models.CharField(max_length=250, null=True)
    secured = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    class Meta:
        ordering = ('type',)

    def __str__(self):
        return '{} {}'.format(self.type, self.text)
