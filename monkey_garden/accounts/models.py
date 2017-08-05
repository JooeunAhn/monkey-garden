from django.conf import settings
from django.db import models

from fcm.models import AbstractDevice


class UserDevice(AbstractDevice):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
