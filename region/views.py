from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions


from .serializers import RegionSerializer
from .models import Region


class RegionViewset (viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = RegionSerializer


