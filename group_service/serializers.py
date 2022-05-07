from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import GroupService


class GroupServiceSerializer (serializers.ModelSerializer):

    group_name = serializers.CharField(source='group', required=False)
    service_type_name = serializers.CharField(source='service_type', required=False)

    class Meta:
        model = GroupService
        fields = ['id',
                  'group',
                  'service_type',
                  'created_by',

                  'group_name',
                  'service_type_name',
                  ]
        validators = [
            UniqueTogetherValidator(
                queryset=GroupService.objects.all(),
                fields=['group', 'service_type'],
                message="The same group cannot have the same service type more than once"
            )
        ]
        read_only_fields = ('id',)


