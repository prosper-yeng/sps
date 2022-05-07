from rest_framework import serializers
from .models import PollingStation


class PollingStationSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = PollingStation
        fields = ['id', 'constituency', 'name_of_polling_station','voters_population', 'polling_station_code', 'status']
