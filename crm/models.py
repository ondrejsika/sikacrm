from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    account = models.ForeignKey(Account, null=True, blank=True)

    name = models.CharField(max_length=32)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    www = models.URLField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class Case(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    account = models.ForeignKey(Account, null=True, blank=True)

    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class EmailAccount(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('auth.User', null=True, blank=True)

    email = models.EmailField()

    smtp_host = models.CharField(max_length=64, null=True, blank=True)
    smtp_port = models.IntegerField(null=True, blank=True)
    smtp_user = models.CharField(max_length=64, null=True, blank=True)
    smtp_password = models.CharField(max_length=64, null=True, blank=True)
    smtp_tls = models.BooleanField(default=True)

    imap_host = models.CharField(max_length=64, null=True, blank=True)
    imap_port = models.IntegerField(null=True, blank=True)
    imap_user = models.CharField(max_length=64, null=True, blank=True)
    imap_password = models.CharField(max_length=64, null=True, blank=True)
    imap_tls = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s #%s' % (self.email, self.id)


class Email(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    case = models.ForeignKey(Case, null=True, blank=True)

    email_account = models.ForeignKey(EmailAccount, related_name='email_set')

    email_from = models.CharField(max_length=256, null=True, blank=True)
    email_to = models.EmailField(max_length=256, null=True, blank=True)

    folder = models.CharField(max_length=16, choices=(
        ('inbox', 'Inbox'),
        ('outbox', 'Outbox'),
    ))

    subject = models.CharField(max_length=256, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Email #%s' % (self.id)
