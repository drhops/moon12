# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table('artful_topic')

        # Adding model 'Artist'
        db.create_table('artful_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=25, unique=True, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(db_index=True, max_length=25, unique=True, null=True, blank=True)),
            ('short_bio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('artful', ['Artist'])


    def backwards(self, orm):
        # Adding model 'Topic'
        db.create_table('artful_topic', (
            ('username', self.gf('django.db.models.fields.CharField')(blank=True, unique=True, max_length=25, null=True, db_index=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('short_bio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, unique=True, max_length=25, null=True, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('artful', ['Topic'])

        # Deleting model 'Artist'
        db.delete_table('artful_artist')


    models = {
        'artful.artist': {
            'Meta': {'object_name': 'Artist'},
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'short_bio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['artful']