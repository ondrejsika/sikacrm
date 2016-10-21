# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Campaign.subject_template'
        db.add_column(u'mailing_campaign', 'subject_template',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=128),
                      keep_default=False)

        # Adding field 'Campaign.body_template'
        db.add_column(u'mailing_campaign', 'body_template',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'Campaign.is_html'
        db.add_column(u'mailing_campaign', 'is_html',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'CampaignEmail.body'
        db.delete_column(u'mailing_campaignemail', 'body')

        # Deleting field 'CampaignEmail.is_sent'
        db.delete_column(u'mailing_campaignemail', 'is_sent')

        # Deleting field 'CampaignEmail.is_html'
        db.delete_column(u'mailing_campaignemail', 'is_html')

        # Deleting field 'CampaignEmail.subject'
        db.delete_column(u'mailing_campaignemail', 'subject')

        # Adding field 'CampaignEmail.in_queue'
        db.add_column(u'mailing_campaignemail', 'in_queue',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CampaignEmail.variables'
        db.add_column(u'mailing_campaignemail', 'variables',
                      self.gf('django.db.models.fields.TextField')(default=u'{}'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Campaign.subject_template'
        db.delete_column(u'mailing_campaign', 'subject_template')

        # Deleting field 'Campaign.body_template'
        db.delete_column(u'mailing_campaign', 'body_template')

        # Deleting field 'Campaign.is_html'
        db.delete_column(u'mailing_campaign', 'is_html')

        # Adding field 'CampaignEmail.body'
        db.add_column(u'mailing_campaignemail', 'body',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'CampaignEmail.is_sent'
        db.add_column(u'mailing_campaignemail', 'is_sent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CampaignEmail.is_html'
        db.add_column(u'mailing_campaignemail', 'is_html',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CampaignEmail.subject'
        db.add_column(u'mailing_campaignemail', 'subject',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=128),
                      keep_default=False)

        # Deleting field 'CampaignEmail.in_queue'
        db.delete_column(u'mailing_campaignemail', 'in_queue')

        # Deleting field 'CampaignEmail.variables'
        db.delete_column(u'mailing_campaignemail', 'variables')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mailing.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'body_template': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_html': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailing.List']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'subject_template': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'mailing.campaignemail': {
            'Meta': {'object_name': 'CampaignEmail'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailing.Campaign']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_to': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'variables': ('django.db.models.fields.TextField', [], {'default': "u'{}'"})
        },
        u'mailing.list': {
            'Meta': {'object_name': 'List'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'mailing.listemail': {
            'Meta': {'object_name': 'ListEmail'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailing.List']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mailing']