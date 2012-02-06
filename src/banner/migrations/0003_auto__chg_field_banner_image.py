# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Banner.image'
        db.alter_column('banner_banner', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Banner.image'
        db.alter_column('banner_banner', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))


    models = {
        'banner.banner': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Banner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['banner']
