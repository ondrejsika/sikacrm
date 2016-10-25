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


class EmailConversationInline(admin.TabularInline):
    model = EmailConversation
    extra = 0


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
    inlines = (
        EmailConversationInline,
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


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class EmailConversationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'case',

        'email_account',
    )
    list_filter = (
        'email_account',
        'case',
    )
    inlines = (
        EmailInline,
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(EmailAccount)
admin.site.register(EmailAccountFolder)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailConversation, EmailConversationAdmin)
admin.site.register(EmailConversationReference)
