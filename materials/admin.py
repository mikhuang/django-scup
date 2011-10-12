from django.contrib import admin
from materials.models import *

class MaterialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Material, MaterialAdmin)