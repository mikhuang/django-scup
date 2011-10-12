# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Material'
        db.create_table('materials_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('materials', ['Material'])


    def backwards(self, orm):
        
        # Deleting model 'Material'
        db.delete_table('materials_material')


    models = {
        'materials.material': {
            'Meta': {'object_name': 'Material'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['materials']
