from rest_framework import serializers

from .models import Message, MessageHistory


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ('author', 'text', 'url', 'latlng',)


class MessageHistorySerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True)

    class Meta:
        model = MessageHistory
        fields = ('message')
