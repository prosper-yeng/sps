from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions


from .serializers import ElectoralAreaSerializer
from .models import ElectoralArea


class ElectoralAreaViewset (viewsets.ModelViewSet):
    queryset = ElectoralArea.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = ElectoralAreaSerializer


