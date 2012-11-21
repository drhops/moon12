# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('artful_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artful.Artist'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('medium', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dimensions', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('artful', ['Image'])

        # Deleting field 'Artist.website'
        db.delete_column('artful_artist', 'website')

        # Deleting field 'Artist.short_bio'
        db.delete_column('artful_artist', 'short_bio')

        # Deleting field 'Artist.email'
        db.delete_column('artful_artist', 'email')

        # Adding field 'Artist.description'
        db.add_column('artful_artist', 'description',
                      self.gf('django.db.models.fields.TextField')(default=datetime.datetime(2012, 11, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'Artist.home_image'
        db.add_column('artful_artist', 'home_image',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('artful_image')

        # Adding field 'Artist.website'
        db.add_column('artful_artist', 'website',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artist.short_bio'
        db.add_column('artful_artist', 'short_bio',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artist.email'
        db.add_column('artful_artist', 'email',
                      self.gf('django.db.models.fields.EmailField')(blank=True, unique=True, max_length=25, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Artist.description'
        db.delete_column('artful_artist', 'description')

        # Deleting field 'Artist.home_image'
        db.delete_column('artful_artist', 'home_image')


    models = {
        'artful.artist': {
            'Meta': {'object_name': 'Artist'},
            'description': ('django.db.models.fields.TextField', [], {}),
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