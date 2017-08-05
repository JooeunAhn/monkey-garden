from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile, UserDevice


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(max_length=1000, blank=True)
    url = models.URLField(blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def lat(self):
        if self.latlng:
            return self.latlng.split(',')[0]
        return None

    @property
    def lng(self):
        if self.latlng:
            return self.latlng.split(',')[1]
        return None


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
        users = users.select_related('profile')
        users = users.filter(profile__last_lat__gte=profile.last_lat-0.001)
        users = users.filter(profile__last_lat__lte=profile.last_lat+0.001)
        users = users.filter(profile__last_lng__gte=profile.last_lng-0.001)
        users = users.filter(profile__last_lng__gte=profile.last_lng+0.001)

        objs = [MessageHistory(user=user, message=instance) for user in users]
        devices = UserDevice.objects.filter(user__in=users)
        MessageHistory.objects.bulk_create(objs)
        devices.send_message({'message': 'Kkik!'}, to='/topics/noti')
