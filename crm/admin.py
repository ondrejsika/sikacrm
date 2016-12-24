import datetime

from django.contrib import admin

from models import Account, Case, Contact, Email, EmailAccount, EmailAccountFolder, EmailConversation,\
    EmailConversationReference, Tag, Contract


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class ContractInline(admin.TabularInline):
    model = Contract
    extra = 0


class CaseInline(admin.TabularInline):
    model = Case
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_activity',
        'next_activity',

        '_get_num_cases',
        '_get_num_contracts',

        'owner',
        'tag',
    )
    list_filter = (
        'last_activity',
        'next_activity',
        'owner',
        'tag',
    )
    inlines = (
        ContactInline,
        CaseInline,
        ContractInline,
    )

    def _get_num_cases(self, obj):
        return obj.case_set.all().count()
    _get_num_cases.short_description = 'Num. Cases'
    # _get_num_emails.admin_order_field = ...

    def _get_num_contracts(self, obj):
        return obj.contract_set.all().count()
    _get_num_contracts.short_description = 'Num. Contr.'


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

        '_get_num_conversations',

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

    def _get_num_conversations(self, obj):
        return obj.emailconversation_set.all().count()
    _get_num_conversations.short_description = 'Num. Conv.'
    # _get_num_conversations.admin_order_field = ...



class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'account',
        'price',
        'length',

        'owner',
        'tag',
    )
    list_filter = (
        'account',

        'owner',
        'tag',
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

        '_get_num_emails',

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

    def _get_num_emails(self, obj):
        return obj.email_set.all().count()
    _get_num_emails.short_description = 'Num. emails'
    # _get_num_emails.admin_order_field = ...

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
admin.site.register(Contract, ContractAdmin)
admin.site.register(EmailAccount, EmailAccountAdmin)
admin.site.register(EmailAccountFolder)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailConversation, EmailConversationAdmin)
admin.site.register(EmailConversationReference)
