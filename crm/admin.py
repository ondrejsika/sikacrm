import datetime

from django.contrib import admin

from models import Account, Case, Contact, Email, EmailAccount, EmailAccountFolder, EmailConversation,\
    EmailConversationReference, Tag, Contract
from workspace.admin_common import WorkspaceAdminMixin


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class ContractInline(admin.TabularInline):
    model = Contract
    extra = 0


class CaseInline(admin.TabularInline):
    model = Case
    extra = 0


class AccountAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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


class ContactAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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


class EmailConversationInline(WorkspaceAdminMixin, admin.TabularInline):
    model = EmailConversation
    extra = 0


class IsOpenCaseFilter(WorkspaceAdminMixin, admin.SimpleListFilter):
    title = 'Is Open'
    parameter_name = 'is_open'

    def lookups(self, request, model_admin):
        return (
            ('open', 'Open'),
            ('closed', 'Closed'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'open':
            return queryset.filter(state__in=Case.OPEN_STATES)
        if self.value() == 'closed':
            return queryset.filter(state__in=Case.CLOSED_STATES)


class CaseAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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
        IsOpenCaseFilter,
        'state',

        'owner',
        'tag',

        'account',
    )
    # inlines = (
    #     EmailConversationInline,
    # )

    def _get_num_conversations(self, obj):
        return obj.emailconversation_set.all().count()
    _get_num_conversations.short_description = 'Num. Conv.'
    # _get_num_conversations.admin_order_field = ...


class ContractAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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


class EmailAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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


class EmailInline(WorkspaceAdminMixin, admin.TabularInline):
    model = Email
    extra = 0


class EmailConversationAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
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


class EmailAccountFolderInline(WorkspaceAdminMixin, admin.TabularInline):
    model = EmailAccountFolder
    extra = 0


class EmailAccountAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
    inlines = (
        EmailAccountFolderInline,
    )


class TagAdmin(WorkspaceAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(EmailAccount, EmailAccountAdmin)
admin.site.register(EmailAccountFolder)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailConversation, EmailConversationAdmin)
admin.site.register(EmailConversationReference)
