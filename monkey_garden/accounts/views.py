from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework import viewsets
from rest_auth.registration.views import SocialLoginView

from accounts.models import UserDevice
from accounts.serializers import UserDeviceSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserDeviceViewSet(viewsets.ModelViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer
