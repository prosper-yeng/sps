from rest_framework import serializers, fields
import datetime

from .models import Permission


class PermissionSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Permission
        fields = ['name',
                  'status']
        extra_kwargs = {'id': {'read_only': True}}

