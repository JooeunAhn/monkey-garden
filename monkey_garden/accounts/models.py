from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from fcm.models import AbstractDevice


class UserDevice(AbstractDevice):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    last_latlng = models.CharField(max_length=100, blank=True)

    @property
    def last_lat(self):
        if self.latlng:
            return self.latlng.split(',')[0]
        return None

    @property
    def last_lng(self):
        if self.latlng:
            return self.latlng.split(',')[1]
        return None


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
