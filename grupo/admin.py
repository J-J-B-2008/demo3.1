from django.contrib import admin
from grupo.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Group)    
