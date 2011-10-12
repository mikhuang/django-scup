from django.contrib import admin
from tournaments.models import *

class TournamentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tournament, TournamentAdmin)