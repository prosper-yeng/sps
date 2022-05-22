# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import StatusSerializer
from .models import Status


class StatusViewset (viewsets.ModelViewSet):
    queryset = Status.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = StatusSerializer


