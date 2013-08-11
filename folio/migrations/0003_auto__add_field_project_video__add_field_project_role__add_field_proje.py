# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.video'
        db.add_column(u'folio_project', 'video',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.role'
        db.add_column(u'folio_project', 'role',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)

        # Adding field 'Project.technologies'
        db.add_column(u'folio_project', 'technologies',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.video'
        db.delete_column(u'folio_project', 'video')

        # Deleting field 'Project.role'
        db.delete_column(u'folio_project', 'role')

        # Deleting field 'Project.technologies'
        db.delete_column(u'folio_project', 'technologies')


    models = {
        u'folio.project': {
            'Meta': {'ordering': "['title']", 'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140'}),
            'technologies': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['folio']