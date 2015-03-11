# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.s1'
        db.add_column(u'crm_client', 's1',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Client.s2'
        db.add_column(u'crm_client', 's2',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Client.s3'
        db.add_column(u'crm_client', 's3',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.s1'
        db.delete_column(u'crm_client', 's1')

        # Deleting field 'Client.s2'
        db.delete_column(u'crm_client', 's2')

        # Deleting field 'Client.s3'
        db.delete_column(u'crm_client', 's3')


    models = {
        u'crm.client': {
            'Meta': {'object_name': 'Client'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            's1': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            's2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            's3': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['crm']