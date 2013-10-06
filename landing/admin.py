from django.contrib import admin

from landing.models import UserRegistered, Mail, Scenario, Speaker


class UserRegisteredAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'token')
    search_fields = ['name', 'email']

admin.site.register(UserRegistered, UserRegisteredAdmin)
admin.site.register(Mail)
admin.site.register(Scenario)
admin.site.register(Speaker)
