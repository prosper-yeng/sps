from rest_framework import serializers

from .models import Status

class StatusSerializer (serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['name']
        extra_kwargs = {'id': {'read_only': True}}

