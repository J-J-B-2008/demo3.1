from django.contrib import admin
from volare.models import GrupoVolare


class FordAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nome', )

admin.site.register(GrupoVolare, FordAdmin)   