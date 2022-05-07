from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions


from .serializers import PollingStationSerializer
from .models import PollingStation


class PollingStationViewset (viewsets.ModelViewSet):
    queryset = PollingStation.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = PollingStationSerializer


