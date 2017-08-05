from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile, UserDevice

sub = lambda val: float(val) - 0.001
add = lambda val: float(val) + 0.001


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(max_length=1000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.latlng != "":
            latlng = self.latlng.split(',')
            self.lat = latlng[0]
            self.lng = latlng[1]
        super(Message, self).save(*args, **kwargs)


class MessageHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.ForeignKey(Message)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    if created:
        user_pk = instance.author.pk
        profile = Profile.objects.get(user=user_pk)
        profile.last_latlng = instance.latlng
        profile.save()
        users = get_user_model().objects.exclude(pk=user_pk)
        users = users.filter(profile__last_lat__gte=sub(profile.last_lat))
        users = users.filter(profile__last_lat__lte=add(profile.last_lat))
        users = users.filter(profile__last_lng__gte=sub(profile.last_lng))
        users = users.filter(profile__last_lng__lte=add(profile.last_lng))

        objs = [MessageHistory(user=user, message=instance) for user in users]
        devices = UserDevice.objects.filter(user__in=users)
        MessageHistory.objects.bulk_create(objs)
        if instance.text == "":
            message = "Kkik!!"
        else:
            message = instance.text
        print(devices)

        devices.send_message({'message': message}, to='/topics/noti')
