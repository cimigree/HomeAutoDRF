from django.db import models

class Api(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=100, blank=True, default='')
    active = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    config = models.TextField()
    # data = JSONField(blank=True, default="")

    class Meta:
        ordering = ('created',)

