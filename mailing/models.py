from __future__ import unicode_literals

from django.db import models


class List(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class ListEmail(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    list = models.ForeignKey(List, null=True, blank=True)

    email = models.EmailField()
    is_unsubscribed = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s #%s' % (self.email, self.id)


class Campaign(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    list = models.ForeignKey(List, null=True, blank=True)

    in_queue = models.BooleanField(default=False)

    name = models.CharField(max_length=32)

    subject_template = models.CharField(max_length=128)
    body_template = models.TextField()
    is_html = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class CampaignEmail(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    campaign = models.ForeignKey(Campaign)

    in_queue = models.BooleanField(default=False)

    email_to = models.EmailField()
    variables = models.TextField(default='{}')

    def __unicode__(self):
        return 'CampaignEmail #%s' % self.id


class QueueEmail(models.Model):
    email_to = models.EmailField()
    email_from = models.EmailField()

    campaign = models.ForeignKey(Campaign, null=True, blank=True)

    subject = models.CharField(max_length=128)
    body = models.TextField()
    is_html = models.BooleanField(default=False)

    is_sent = models.BooleanField(default=False)
    is_failed = models.BooleanField(default=False)

    def __unicode__(self):
        return 'QueueEmail #%s' % self.id


class Unsubscription(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    campaign = models.ForeignKey(Campaign)
    email = models.ForeignKey(ListEmail)

    def __unicode__(self):
        return 'QueueEmail #%s' % self.id
