from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Message, MessageHistory
from .serializers import MessageSerializer, MessageHistorySerializer


class MessageViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )


class MessageHistoryViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        mh = MessageHistory.objects.filter(user=user).order_by("-created_at")
        mh = mh.exclude(message_url='')[:3]
        return mh
