from rest_framework import serializers

from .models import District

class DistrictSerializer (serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ['id', 'region','name_of_district','status']

