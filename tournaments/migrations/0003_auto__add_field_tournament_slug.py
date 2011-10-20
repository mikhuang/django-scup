# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.template.defaultfilters import slugify

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tournament.slug'
        db.add_column('tournaments_tournament', 'slug', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50, db_index=True, null=True), keep_default=False)
        
        for tournament in orm.Tournament.objects.all():
            name = slugify(tournament.name)
            tournament.slug = name # warning: possible that slugs aren't unique to year
            tournament.save()

    def backwards(self, orm):
        
        # Deleting field 'Tournament.slug'
        db.delete_column('tournaments_tournament', 'slug')


    models = {
        'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['tournaments']
