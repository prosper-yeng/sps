import pytz
from django.db import models
from django.contrib.auth.models import User

# from users.models import CustomUser
from choice.views import StatusChoice, AddressTypeChoice


class Address ( models.Model ):
    user = models.ForeignKey ( User, on_delete=models.CASCADE, related_name='person' )
    address_type = models.ForeignKey ( 'select_item.SelectItem', on_delete=models.CASCADE, related_name='address_type' )
    country = models.CharField ( max_length=100, choices=pytz.country_names.items (),
                                 default='GH' )
    region = models.ForeignKey ( 'select_item.SelectItem', on_delete=models.CASCADE, related_name='region' )
    district = models.ForeignKey ( 'select_item.SelectItem', on_delete=models.CASCADE, related_name='district' )
    town = models.ForeignKey ( 'select_item.SelectItem', on_delete=models.CASCADE, related_name='town' )
    street = models.CharField ( max_length=100, null=False, unique=False )
    postcode = models.CharField ( max_length=100, null=False, unique=False, verbose_name='Postcode/Post Box' )
    house_number = models.CharField ( max_length=100, null=False, unique=False, verbose_name=' House Number ' )
    digital_address = models.CharField ( max_length=100, null=True, unique=False, verbose_name=' Digital Address' )
    status = models.CharField ( max_length=100, choices=StatusChoice.choices )
    created_by = models.ForeignKey ( User, on_delete=models.CASCADE, )
    created_on = models.DateTimeField ( auto_now_add=True )
    modified_on = models.DateTimeField ( auto_now=True )

    def __str__(self):
        return '{} {}'.format ( self.person, self.town )
