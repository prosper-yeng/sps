# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import NationalSerializer
from .models import Nation


class DistrictViewset (viewsets.ModelViewSet):
    queryset = Nation.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = NationalSerializer


