# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Image.medium'
        db.alter_column('artful_image', 'medium', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Image.description'
        db.alter_column('artful_image', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Image.title'
        db.alter_column('artful_image', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Image.source'
        db.alter_column('artful_image', 'source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Image.year'
        db.alter_column('artful_image', 'year', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Image.dimensions'
        db.alter_column('artful_image', 'dimensions', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding field 'Artist.statement'
        db.add_column('artful_artist', 'statement',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Artist.description'
        db.alter_column('artful_artist', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Artist.display_order'
        db.alter_column('artful_artist', 'display_order', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Image.medium'
        raise RuntimeError("Cannot reverse this migration. 'Image.medium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.description'
        raise RuntimeError("Cannot reverse this migration. 'Image.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.title'
        raise RuntimeError("Cannot reverse this migration. 'Image.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.source'
        raise RuntimeError("Cannot reverse this migration. 'Image.source' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.year'
        raise RuntimeError("Cannot reverse this migration. 'Image.year' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.dimensions'
        raise RuntimeError("Cannot reverse this migration. 'Image.dimensions' and its values cannot be restored.")
        # Deleting field 'Artist.statement'
        db.delete_column('artful_artist', 'statement')


        # User chose to not deal with backwards NULL issues for 'Artist.description'
        raise RuntimeError("Cannot reverse this migration. 'Artist.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Artist.display_order'
        raise RuntimeError("Cannot reverse this migration. 'Artist.display_order' and its values cannot be restored.")

    models = {
        'artful.artist': {
            'Meta': {'object_name': 'Artist'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'home_image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'statement': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'artful.image': {
            'Meta': {'object_name': 'Image'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artful.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['artful']