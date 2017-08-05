from rest_framework import serializers

from accounts.models import UserDevice


class UserDeviceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserDevice
        fields = ("dev_id", "reg_id", "name", "is_active", "user")
