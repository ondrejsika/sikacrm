from django.contrib import admin

from models import Workspace


class WorkspaceAdminMixin(object):
    @staticmethod
    def get_or_create_workspace(request):
        name = request.session.get('workspace_name')
        workspace, created = Workspace.objects.get_or_create(user=request.user, name=name or Workspace.DEFAULT_NAME)
        if created:
            workspace.save()

        return workspace

    @staticmethod
    def set_workspace(request, name):
        request.session['workspace_name'] = name
        request.session.save()

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        workspace = self.get_or_create_workspace(request)
        return qs.filter(workspace=workspace)

