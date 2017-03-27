from __future__ import unicode_literals

from django.db import models


class Workspace(models.Model):
    DEFAULT_NAME = '<default>'

    # group = models.ForeignKey('WorkspaceGroup')
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=64, default=DEFAULT_NAME)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)

    class Meta(object):
        unique_together = ('name', 'user')

# class WorkspaceGroup(models.Model):
#     name = models.CharField(max_length=64)
#     users = models.ManyToManyField('auth.User')
#
#     def __unicode__(self):
#         return '%s #%s' % (self.name, self.id)
#
#     def get_default_workspace(self):
#         try:
#             self.workspace_set.get(name__isnull=True)
#         except Workspace.DoesNotExist:
#             return None
