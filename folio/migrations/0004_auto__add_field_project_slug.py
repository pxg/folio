# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.slug'
        db.add_column(u'folio_project', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=140, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.slug'
        db.delete_column(u'folio_project', 'slug')


    models = {
        u'folio.project': {
            'Meta': {'ordering': "['title']", 'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True'}),
            'technologies': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['folio']