from django.contrib import admin
from .models import LeadBasica

class ListandoLead(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('id','nome','desnivel','vazao','potencia','mchs')
    list_display_links = ('id', 'nome')

admin.site.register(LeadBasica, ListandoLead)

