from rest_framework import serializers
from .models import Constituency


class ConstituencySerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Constituency
        fields = ['id',  'name_of_constituency','constituency_code','region', 'district', 'status']
