from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    name = models.CharField(max_length=32)

    company_id = models.CharField(max_length=32, null=True, blank=True)
    vat_id = models.CharField(max_length=32, null=True, blank=True)

    contact_address = models.TextField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    www = models.URLField(null=True, blank=True)

    note = models.TextField(null=True, blank=True)

    last_activity = models.DateField(null=True, blank=True)
    next_activity = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    account = models.ForeignKey(Account, null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    name = models.CharField(max_length=32)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    www = models.URLField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s / %s #%s' % (self.account.name, self.name, self.id)


class Case(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    APPROVED = 'approved'
    DONE = 'done'
    CANCELLED = 'cancelled'

    OPEN_STATES = (NEW, IN_PROGRESS, APPROVED)
    CLOSED_STATES = (CANCELLED, DONE)

    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    account = models.ForeignKey(Account, null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    state = models.CharField(max_length=16, default=NEW, choices=(
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (APPROVED, 'Approved'),
        (DONE, 'Done'),
        (CANCELLED, 'Cancelled'),
    ))

    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s / %s #%s' % (self.account.name, self.name, self.id)


class Contract(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', null=True, blank=True)
    account = models.ForeignKey(Account, null=True, blank=True)
    case = models.ForeignKey(Case, null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    start_at = models.DateField()
    price = models.IntegerField()
    length = models.IntegerField(help_text='Length in hours, day=8h')

    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s / %s #%s' % (self.account.name, self.name, self.id)


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


class EmailAccountFolder(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    email_account = models.ForeignKey(EmailAccount, related_name='folder_set')
    folder = models.CharField(max_length=64)
    last_id = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s %s #%s' % (self.email_account.email, self.folder, self.id)


class EmailConversation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    email_account = models.ForeignKey(EmailAccount, related_name='email_conversation_set')
    case = models.ForeignKey(Case, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        return '%s #%s' % (self.name, self.id)


class EmailConversationReference(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    email_conversation = models.ForeignKey(EmailConversation, null=True, blank=True)

    reference = models.CharField(max_length=256, db_index=True)

    def __unicode__(self):
        return 'EmailConversationReference #%s' % self.id


class Email(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    email_conversation = models.ForeignKey(EmailConversation)

    email_account = models.ForeignKey(EmailAccount, related_name='email_set')

    message_id = models.CharField(max_length=256)

    date = models.DateTimeField()
    email_from = models.CharField(max_length=256, null=True, blank=True)
    email_to = models.CharField(max_length=256, null=True, blank=True)

    folder = models.CharField(max_length=16, choices=(
        ('inbox', 'Inbox'),
        ('outbox', 'Outbox'),
    ))

    subject = models.CharField(max_length=256, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-date', )

    def __unicode__(self):
        return 'Email #%s' % self.id
