from rest_framework import serializers
from apis.models import Device, HomesService, Service
from django.contrib.auth.models import User

# class JSONSerializerField(serializers.Field):
#     """ Serializer for JSONField -- required to make field writable"""
#     def to_internal_value(self, data):
#         return data
#     def to_representation(self, value):
#         return value


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'type', 'hostname')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    defaultconfig = serializers.JSONField(binary = 'true')
    
    class Meta:
        model = Service
        fields = ('id', 'name', 'defaultconfig')

class HomesServiceSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.ChoiceField(choices=list(Device.objects.all().values_list('name', flat=False)))
    service = serializers.ChoiceField(choices=list(Service.objects.all().values_list('name', flat=False)))
    config = serializers.JSONField(binary='true')

    class Meta:
        model = HomesService
        fields = ('id', 'device', 'service', 'active', 'config')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

