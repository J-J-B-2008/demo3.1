from django.contrib import admin
from app.models import Montadora, Unidade, Grupo, Fabricante, Produtos

class AppAdmin(admin.ModelAdmin ):
    list_display = ('id', 'nome',)


admin.site.register(Montadora, AppAdmin )
admin.site.register(Unidade, AppAdmin)
admin.site.register(Grupo, AppAdmin)
admin.site.register(Fabricante, AppAdmin) 


class ProdAppAdmin(admin.ModelAdmin):
    list_display = ('codigo','descricao','aplicacao')
    search_fields = ('codigo', 'descricao')

    
admin.site.register(Produtos, ProdAppAdmin)    
