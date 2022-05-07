from rest_framework import serializers
from .models import PollingStation


class PollingStationSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = PollingStation
        fields = ['id', 'name_of_polling_station','voters_population', 'polling_station_code','electoral_area', 'status']
