from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    www = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    s1 = models.NullBooleanField()
    s2 = models.NullBooleanField()
    s3 = models.NullBooleanField()
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s #%s' % (self.name, self.id)


class Project(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=128)
    s1 = models.NullBooleanField()
    s2 = models.NullBooleanField()
    s3 = models.NullBooleanField()
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s #%s' % (self.name, self.id)


class Hosting(models.Model):
    project = models.ForeignKey(Project)
    actual_price = models.IntegerField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'Hosting: %s #%s' % (self.project.name, self.id)


class HostingPayment(models.Model):
    hosting = models.ForeignKey(Hosting)
    price = models.IntegerField()
    description = models.CharField(max_length=256, null=True, blank=True)
    timestamp_dt = models.DateTimeField(auto_now_add=True)
    payed_to_dt = models.DateField()

    def __unicode__(self):
        return u'Hosting payment #%s' % (self.id)

    class Meta:
        ordering = ('-timestamp_dt', )
