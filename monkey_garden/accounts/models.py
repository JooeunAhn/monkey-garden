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
    last_lat = models.FloatField(default=0)
    last_lng = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.last_latlng != "":
            latlng = self.last_latlng.split(',')
            self.last_lat = latlng[0]
            self.last_lng = latlng[1]
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
