# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artist.display_order'
        db.add_column('artful_artist', 'display_order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artist.display_order'
        db.delete_column('artful_artist', 'display_order')


    models = {
        'artful.artist': {
            'Meta': {'object_name': 'Artist'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_order': ('django.db.models.fields.IntegerField', [], {}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'home_image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'artful.image': {
            'Meta': {'object_name': 'Image'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artful.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['artful']