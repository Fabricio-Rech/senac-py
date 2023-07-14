from django.contrib import admin
from . import models

class TipoFenderAdmin(admin.ModelAdmin):
    # 
    ...

admin.site.register(models.TipoFender, TipoFenderAdmin)