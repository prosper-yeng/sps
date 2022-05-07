
from django.http import request
from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect


class StatusChoice ( models.TextChoices ):
    CREATED = 'created', 'Created'
    APPROVED = 'approved', 'Approved'
    ACTIVE = 'active', 'Active'
    DEACTIVATE = 'deactivate', 'Deactivate'
    DELETE = 'delete', 'Delete'
    CLOSED = 'closed', 'Closed'





class GenderChoice ( models.TextChoices ):
    FEMALE = 'female', 'Female'
    MALE = 'male', 'Male'

class DistrictChoice ( models.TextChoices ):
    JIRAPA = 'jirapa', 'Jirapa'
    SUNYANI = 'sunyani', 'Sunyani'


class MaritalChoice ( models.TextChoices ):
    SINGLE = 'single', 'Single'
    MARRIED = 'married', 'Married'







class OccupationChoice ( models.TextChoices ):
    FARMER = 'farmer', 'Farmer'
    TEACHER = 'teacher', 'Teacher'


class TitleChoice ( models.TextChoices ):
    MR = 'mr', 'Mr'
    MISS = 'miss', 'Miss'
    MRS = 'mrs', 'Mrs'



def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


