from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions


from .serializers import ConstituencySerializer
from .models import Constituency


class ConstituencyViewset (viewsets.ModelViewSet):
    queryset = Constituency.objects.all()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = ConstituencySerializer


