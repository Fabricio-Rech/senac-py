from django.contrib import admin
from . import models

class TipoAdmin(admin.ModelAdmin):
    # 
    ...

admin.site.register(models.Tipo, TipoAdmin)