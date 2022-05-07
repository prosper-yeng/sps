from rest_framework import serializers, fields
import datetime

from .models import Region


class RegionSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Region
        fields = ['id', 'nation', 'name_of_region', 'regional_code', 'status']
