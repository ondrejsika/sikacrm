from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'www',
        'email',
        's1',
        's2',
        's3',
        'created',
        'last_update',
        'owner',
    )


admin.site.register(Client, ClientAdmin)