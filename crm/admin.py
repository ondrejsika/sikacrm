import datetime

from django.contrib import admin

from .models import Client, Hosting, Project, HostingPayment


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
    list_filter = (
        's1',
        's2',
        's3',
        'owner',
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'client',
        's1',
        's2',
        's3',
        'owner',
    )
    list_filter = (
        'client',
    )


class HostingPaymentInline(admin.TabularInline):
    model = HostingPayment
    extra = 0


class HostingAdmin(admin.ModelAdmin):
    def _is_payed(obj):
        last = obj.hostingpayment_set.first()
        if not last:
            return 'NO (never payed)'
        if last.payed_to_dt > datetime.date.today():
            return 'YES (to %s, +%s days)' % (last.payed_to_dt, (last.payed_to_dt - datetime.date.today()).days)
        return 'NO (to %s, -%s days)' % (last.payed_to_dt, (datetime.date.today() - last.payed_to_dt).days)

    list_display = (
        'project',
        lambda obj: obj.project.client,
        'is_active',
        _is_payed,
    )
    inlines = (
        HostingPaymentInline,
    )


class HostingPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'hosting',
        'price',
        'timestamp_dt',
        'payed_to_dt',
    )
    list_filter = (
        'hosting',
    )

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Hosting, HostingAdmin)
admin.site.register(HostingPayment, HostingPaymentAdmin)
