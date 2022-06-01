from django.contrib import admin
from .models import LeadAvancada, Bitola, Conexoe

class ListandoLead(admin.ModelAdmin):
    list_display = ('id', "nome")
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('modelo',)
    list_per_page = 30

class ListandoBitola(admin.ModelAdmin):
    list_display = ('id', "bitola","corrente")
    list_display_links = ('id', 'bitola')
    search_fields = ('bitola',)
    list_per_page = 30

class ListandoConexoe(admin.ModelAdmin):
    list_display = ('id', "nome_conex",'k')
    list_display_links = ('id', 'nome_conex')
    search_fields = ('nome_conex',)
    list_per_page = 30

admin.site.register(LeadAvancada, ListandoLead)
admin.site.register(Bitola, ListandoBitola)
admin.site.register(Conexoe, ListandoConexoe)
