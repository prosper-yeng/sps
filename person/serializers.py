from rest_framework import serializers
from django.contrib.auth.models import User, Group

#from .models import Patient, Staff


class UserSerializer(serializers.ModelSerializer):

    #group_name = serializers.CharField(source='group.name', required=False)
    #gender_name = serializers.CharField(source='gender.text', required=False)
    #nationality_name = serializers.CharField(source='nationality.text', required=False)

    class Meta:
        model = User
        fields = (
                  'username',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'date_of_birth',
                  'gender',
                  'email',
                  'national_id',
                  'primary_phone',
                  'secondary_phone',
                  'photo_url',
                  'group',
                  'region',
                  'constituency',
                  'polling_station',
                  'password',
                  'old_pwd',
                  'created_by',
                  )

        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

'''
class PatientSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)

    title_name = serializers.CharField(source='title.text', required=False)
    occupation_name = serializers.CharField(source='occupation.text', required=False)
    marital_status_name = serializers.CharField(source='marital_status.text', required=False)
    religion_name = serializers.CharField(source='religion.text', required=False)

    facility_name = serializers.CharField(source='user.facility', required=False)
    email = serializers.CharField(source='user.email', required=False)

    class Meta:
        model = Patient
        fields = ('id',
                  'title',
                  'marital_status',
                  'occupation',
                  'contact_name',
                  'contact_phone',
                  'contact_email',
                  'resident_address',
                  'religion',

                  'full_name',
                  'title_name',
                  'occupation_name',
                  'marital_status_name',
                  'religion_name',

                  'facility_name',
                  'email',

                  'user',
                  )

        read_only_fields = ('id',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.get('password')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        patient = Patient.objects.create(user=user, **validated_data)

        return patient

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user')
        instance.title = validated_data.get('title', instance.title)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.contact_phone = validated_data.get('contact_phone', instance.contact_phone)
        instance.contact_email = validated_data.get('contact_email', instance.contact_email)
        instance.resident_address = validated_data.get('resident_address', instance.resident_address)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.save()

        uid = instance.user_id

        user = User.objects.get(id=uid)

        user.facility = user_data.get('facility', user.facility)
        user.group = user_data.get('group', user.group)
        user.first_name = user_data.get('first_name', user.first_name)
        user.middle_name = user_data.get('middle_name', user.middle_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.date_of_birth = user_data.get('date_of_birth', user.date_of_birth)
        user.gender = user_data.get('gender', user.gender)
        user.email = user_data.get('email', user.email)
        user.nationality = user_data.get('nationality', user.nationality)
        user.national_id = user_data.get('national_id', user.national_id)
        user.primary_phone = user_data.get('primary_phone', user.primary_phone)
        user.secondary_phone = user_data.get('secondary_phone', user.secondary_phone)
        user.photo_url = user_data.get('photo_url', user.photo_url)
        user.password = user_data.get('password', user.password)

        user.save()

        return instance


class StaffSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)

    facility_name = serializers.CharField(source='user.facility', required=False)
    email = serializers.CharField(source='user.email', required=False)
    first_name = serializers.CharField(source='user.first_name', required=False)
    middle_name = serializers.CharField(source='user.middle_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    occupation_name = serializers.CharField(source='occupation.text', required=False)
    marital_status_name = serializers.CharField(source='marital_status.text', required=False)
    religion_name = serializers.CharField(source='religion.text', required=False)

    class Meta:
        model = Staff
        fields = ('id',
                  'facility_name',
                  'title',
                  'occupation',
                  'marital_status',
                  'contact_name',
                  'contact_phone',
                  'contact_email',
                  'religion',

                  'first_name',
                  'middle_name',
                  'last_name',
                  'full_name',
                  'email',
                  'occupation_name',
                  'marital_status_name',
                  'resident_address',
                  'religion_name',

                  'user',
                  )

        read_only_fields = ('id',)

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        password = user_data.get('password')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        staff = Staff.objects.create(user=user, **validated_data)

        return staff

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.title = validated_data.get('title', instance.title)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.contact_phone = validated_data.get('contact_phone', instance.contact_phone)
        instance.contact_email = validated_data.get('contact_email', instance.contact_email)
        instance.resident_address = validated_data.get('resident_address', instance.resident_address)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.save()

        uid = instance.user_id

        user = User.objects.get(id=uid)

        user.facility = user_data.get('facility', user.facility)
        user.group = user_data.get('group', user.group)
        user.first_name = user_data.get('first_name', user.first_name)
        user.middle_name = user_data.get('middle_name', user.middle_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.date_of_birth = user_data.get('date_of_birth', user.date_of_birth)
        user.gender = user_data.get('gender', user.gender)
        user.email = user_data.get('email', user.email)
        user.nationality = user_data.get('nationality', user.nationality)
        user.national_id = user_data.get('national_id', user.national_id)
        user.primary_phone = user_data.get('primary_phone', user.primary_phone)
        user.secondary_phone = user_data.get('secondary_phone', user.secondary_phone)
        user.photo_url = user_data.get('photo_url', user.photo_url)
        user.password = user_data.get('password', user.password)

        user.save()

        return instance

'''

class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'default_pwd_changed',
                  'username',
                  'email',
                  'password']
        extra_kwargs = {'default_pwd': {'write_only': True},
                        'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None )
        # pref_language = validated_data.pop('pref_language', None )
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # instance.save ( pref_language )
            instance.save()
            return instance
