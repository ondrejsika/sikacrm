import datetime

from django.contrib import admin

from models import Account, Case, Contact, Email, EmailAccount, EmailAccountFolder, EmailConversation, EmailConversationReference


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',

        'owner',
    )
    list_filter = (
        'owner',
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'name',
        'email',
        'phone',

        'owner',
    )
    list_filter = (
        'account',

        'owner',
    )


class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'account',

        'owner',
    )
    list_filter = (
        'account',

        'owner',
    )


class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subject',
        'date',
        'email_from',
        'email_to',
        'email_conversation',

        'email_account',
    )
    list_filter = (
        'email_from',
        'email_to',
        'email_conversation',

        'email_account',
    )


class EmailConversationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'account',

        'owner',
    )
    list_filter = (
        'account',

        'owner',
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(EmailAccount)
admin.site.register(EmailAccountFolder)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailConversation)
admin.site.register(EmailConversationReference)
