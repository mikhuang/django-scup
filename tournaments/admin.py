from django.contrib import admin
from tournaments.models import *

class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Tournament, TournamentAdmin)