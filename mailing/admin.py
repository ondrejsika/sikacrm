import datetime

from django.contrib import admin

from models import List, ListEmail, Campaign, CampaignEmail, QueueEmail, Unsubscription


class ListAdmin(admin.ModelAdmin):
    list_display = (
        'name',

        'owner',
    )
    list_filter = (
        'owner',
    )


class ListEmailAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'list',
        'is_unsubscribed',

    )
    list_filter = (
        'list',
        'is_unsubscribed',
    )


class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'in_queue',

        'owner',
    )
    list_filter = (
        'list',
        'in_queue',

        'owner',
    )


class CampaignEmailAdmin(admin.ModelAdmin):
    list_display = (
        'email_to',
        'in_queue',

        'campaign',
    )
    list_filter = (
        'campaign',
        'email_to',
    )


class QueueEmailAdmin(admin.ModelAdmin):
    list_display = (
        'email_from',
        'email_to',

        'is_sent',
        'is_failed',
    )
    list_filter = (
        'campaign',

        'is_sent',
        'is_failed',
    )


class UnsubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'campaign',
    )
    list_filter = (
        'email',
        'campaign',
    )

admin.site.register(List, ListAdmin)
admin.site.register(ListEmail, ListEmailAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CampaignEmail, CampaignEmailAdmin)
admin.site.register(QueueEmail, QueueEmailAdmin)
admin.site.register(Unsubscription, UnsubscriptionAdmin)
