from django.contrib.auth.models import User
from apis.models import Device, HomesService, Service
from apis.serializers import DeviceSerializer, HomesServiceSerializer, ServiceSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.response import Response

# from rest_framework.decorators import detail_route

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class HomesServiceViewSet(viewsets.ModelViewSet):
    # device = DeviceSerializer
    # service = ServiceSerializer
    queryset = HomesService.objects.all()
    serializer_class = HomesServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

