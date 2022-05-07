from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import  Address
from .serializers import  AddressSerializer




class AddressViewset (viewsets.ModelViewSet):
    queryset = Address.objects.all ()
    permission = [
        permissions.AllowAny
    ]
    serializer_class = AddressSerializer


