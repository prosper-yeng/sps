from rest_framework import serializers, fields
import datetime

from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        '''['id',
                  'name',
                  'Permissions',
                  'default',
                  'status']
        read_only_fields = ['id', ]
        # extra_kwargs = {'id': {'read_only': True}}'''

    # def to_representation(self, instance):
    #     data = super(GroupSerializer, self).to_representation(instance)
    #     data.created_on = serializers.CharField(source='created_on')
    #     return data


class GroupUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
