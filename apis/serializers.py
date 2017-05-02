from rest_framework import serializers
from apis.models import Api
from django.contrib.auth.models import User

# class JSONSerializerField(serializers.Field):
#     """ Serializer for JSONField -- required to make field writable"""
#     def to_internal_value(self, data):
#         return data
#     def to_representation(self, value):
#         return value

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    config = serializers.JSONField(binary = 'true')
    class Meta:
        model = Api
        fields = ('id', 'label', 'active', 'locked',
                  'config',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
