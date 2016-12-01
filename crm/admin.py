import datetime

from django.contrib import admin

from models import Account, Case, Contact, Email, EmailAccount, EmailAccountFolder, EmailConversation,\
    EmailConversationReference, Tag


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class CaseInline(admin.TabularInline):
    model = Case
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',

        'owner',
        'tag',
    )
    list_filter = (
        'owner',
        'tag',
    )
    inlines = (
        ContactInline,
        CaseInline,
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'name',
        'email',
        'phone',

        'owner',
        'tag',
    )
    list_filter = (
        'account',

        'owner',
        'tag',
    )


class EmailConversationInline(admin.TabularInline):
    model = EmailConversation
    extra = 0


class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'account',
        'state',

        'owner',
        'tag',
    )
    list_filter = (
        'account',
        'state',

        'owner',
        'tag',
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
        'tag',
    )
    list_filter = (
        'email_account',
        'case',
        'tag',
    )
    inlines = (
        EmailInline,
    )


class EmailAccountFolderInline(admin.TabularInline):
    model = EmailAccountFolder
    extra = 0


class EmailAccountAdmin(admin.ModelAdmin):
    inlines = (
        EmailAccountFolderInline,
    )


admin.site.register(Tag)
admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(EmailAccount, EmailAccountAdmin)
admin.site.register(EmailAccountFolder)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailConversation, EmailConversationAdmin)
admin.site.register(EmailConversationReference)
