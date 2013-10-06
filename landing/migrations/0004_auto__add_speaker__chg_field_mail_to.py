# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'landing_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['landing.Scenario'])),
        ))
        db.send_create_signal(u'landing', ['Speaker'])

        # Adding model 'Scenario'
        db.create_table(u'landing_scenario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'landing', ['Scenario'])


        # Changing field 'Mail.to'
        db.alter_column(u'landing_mail', 'to', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'landing_speaker')

        # Deleting model 'Scenario'
        db.delete_table(u'landing_scenario')


        # Changing field 'Mail.to'
        db.alter_column(u'landing_mail', 'to', self.gf('django.db.models.fields.TextField')())

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
            'to': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'landing.scenario': {
            'Meta': {'object_name': 'Scenario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'landing.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['landing.Scenario']"})
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