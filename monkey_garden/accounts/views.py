from django.contrib.auth import get_user_model

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_auth.registration.views import SocialLoginView

from accounts.models import UserDevice
from accounts.serializers import UserDeviceSerializer, UserSerializer

sub = lambda val: float(val) - 0.001
add = lambda val: float(val) + 0.001


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        profile = self.request.user.profile
        lat = profile.last_lat
        lng = profile.last_lng
        users = get_user_model().objects.exclude(profile__last_latlng='')
        users = users.select_related('profile')
        users = users.filter(profile__last_lat__gte=sub(lat))
        users = users.filter(profile__last_lat__lte=add(lat))
        users = users.filter(profile__last_lng__gte=sub(lng))
        users = users.filter(profile__last_lng__lte=add(lng))
        return users


class UserDeviceViewSet(viewsets.ModelViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer
