from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import UserDevice, Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('last_latlng', 'last_lat', 'last_lng',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'profile',)


class UserDeviceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserDevice
        fields = ("dev_id", "reg_id", "name", "is_active", "user")
