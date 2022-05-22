from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractUser
from choice.views import StatusChoice,GenderChoice
from django.utils import timezone

from polling_station.models import PollingStation
from constituency.models import Constituency
from electoral_area.models import ElectoralArea
from region.models import Region
from validator.views import validate_file_size, valid_phone_number
from common.views import allowed_extension
from django.utils.timezone import now

from django.core.validators import FileExtensionValidator
#User.add_to_class('photo_url',   models.CharField(max_length=100000, blank=True, null=True))
User.add_to_class('photo_url',   models.FileField(validators=[validate_file_size, FileExtensionValidator ( allowed_extensions=allowed_extension )], upload_to='persons', verbose_name='Photo', null=True, blank=True ))
User.add_to_class('primary_phone',  models.CharField(validators=[valid_phone_number], max_length=15, verbose_name='Primary Phone',blank=True, null=True ))
User.add_to_class('secondary_phone',  models.CharField(validators=[valid_phone_number], max_length=15, verbose_name='Secondary Phone',  blank=True, null=True ))
User.add_to_class('group',  models.ForeignKey(Group, on_delete=models.CASCADE, default=1,related_name='group'))
User.add_to_class('middle_name', models.CharField(max_length=50, blank=True, null=True, verbose_name='Middle Name'))
User.add_to_class('date_of_birth', models.DateField(default='1818-01-01'))
User.add_to_class('gender',  models.CharField(max_length=10,choices=GenderChoice.choices, blank=True, null=True, ))
User.add_to_class('national_id',  models.CharField(max_length=100, blank=True, null=True))
User.add_to_class('region', models.ForeignKey(Region, on_delete=models.CASCADE, null=True, related_name='user_region_station'))
User.add_to_class('constituency', models.ForeignKey(Constituency, on_delete=models.CASCADE, null=True, related_name='user_constituency'))
User.add_to_class('polling_station', models.ForeignKey(PollingStation, on_delete=models.CASCADE, null=True, related_name='user_polling_station'))
User.add_to_class('electoral_area', models.ForeignKey(ElectoralArea, on_delete=models.CASCADE, null=True, related_name='user_electoral_area'))
Group.add_to_class('default',  models.BooleanField(default=False))
User.add_to_class('default_pwd_changed',  models.BooleanField(default=False,blank=True, null=True ))
User.add_to_class('old_pwd',  models.CharField(max_length=100, blank=True, null=True ))
User.add_to_class('status',   models.ForeignKey ('status.Status', on_delete=models.CASCADE, related_name='person_status' ))
User.add_to_class('created_by',  models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_created_by', max_length=100))
User.add_to_class('created_on',  models.DateTimeField( default=now))









