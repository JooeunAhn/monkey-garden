from django.contrib import admin

from .models import Message, MessageHistory


class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'latlng', 'url']

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageHistory)
