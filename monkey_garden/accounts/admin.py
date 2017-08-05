from django.contrib import admin

from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Profile, ProfileAdmin)
