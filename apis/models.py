from django.db import models

class Service(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    defaultconfig = models.TextField()
    # data = JSONField(blank=True, default="")

    class Meta:
        ordering = ('name',)

    def __str__(self):          
        return self.name

class Device(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)

    class Meta:
        ordering = ('type',)

    def __str__(self):
         return self.name

class HomesService(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    config = models.TextField(default="default field")



# def default_config():
#     configId = self.service_Id
#     return apis_services[configId].defaultconfig
#     or obj.services.defaultconfig;

#     Services.objects.get(id=config_Id).default_config

#     class Meta
#         ordering = ('created')


