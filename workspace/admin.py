from django.contrib import admin

from models import Workspace
from admin_common import WorkspaceAdminMixin


class WorkspaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
    )
    list_filter = (
        'user',
    )

    def save_model(self, request, obj, *args, **kwargs):
        super(WorkspaceAdmin, self).save_model(request, obj, *args, **kwargs)
        WorkspaceAdminMixin.set_workspace(request, obj.name)


admin.site.register(Workspace, WorkspaceAdmin)
