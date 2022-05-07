# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import GroupServiceSerializer
from .models import GroupService


class GroupServiceViewSet(viewsets.ModelViewSet):
    queryset = GroupService.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = GroupServiceSerializer
