from django.db import models


class Client(models.Model):
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    name = models.CharField(max_length=128)
    www = models.URLField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    s1 = models.NullBooleanField()
    s2 = models.NullBooleanField()
    s3 = models.NullBooleanField()
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s #%s' % (self.name, self.id)
