# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import DistrictSerializer
from .models import District


class DistrictViewset (viewsets.ModelViewSet):
    queryset = District.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = DistrictSerializer


