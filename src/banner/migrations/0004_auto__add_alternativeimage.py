# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AlternativeImage'
        db.create_table('banner_alternativeimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='alternatives', to=orm['banner.Banner'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('banner', ['AlternativeImage'])


    def backwards(self, orm):
        
        # Deleting model 'AlternativeImage'
        db.delete_table('banner_alternativeimage')


    models = {
        'banner.alternativeimage': {
            'Meta': {'object_name': 'AlternativeImage'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alternatives'", 'to': "orm['banner.Banner']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        },
        'banner.banner': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Banner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['banner']
