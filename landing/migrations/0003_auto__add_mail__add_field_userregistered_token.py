# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table(u'landing_mail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('to', self.gf('django.db.models.fields.TextField')()),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('reject_reason', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'landing', ['Mail'])

        # Adding field 'UserRegistered.token'
        db.add_column(u'landing_userregistered', 'token',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table(u'landing_mail')

        # Deleting field 'UserRegistered.token'
        db.delete_column(u'landing_userregistered', 'token')


    models = {
        u'landing.mail': {
            'Meta': {'object_name': 'Mail'},
            'data': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reject_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to': ('django.db.models.fields.TextField', [], {})
        },
        u'landing.userregistered': {
            'Meta': {'object_name': 'UserRegistered'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['landing']