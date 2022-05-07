from rest_framework import serializers
from .models import ElectoralArea


class ElectoralAreaSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = ElectoralArea
        fields = ['id',  'name_of_electoral_area','electoral_area_code','constituency', 'status']
