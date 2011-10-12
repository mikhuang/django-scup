# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tournament.location'
        db.add_column('tournaments_tournament', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Tournament.lat'
        db.add_column('tournaments_tournament', 'lat', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'Tournament.lon'
        db.add_column('tournaments_tournament', 'lon', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Tournament.location'
        db.delete_column('tournaments_tournament', 'location')

        # Deleting field 'Tournament.lat'
        db.delete_column('tournaments_tournament', 'lat')

        # Deleting field 'Tournament.lon'
        db.delete_column('tournaments_tournament', 'lon')


    models = {
        'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tournaments']
