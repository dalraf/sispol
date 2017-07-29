# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

class EventoDetalhe(admin.ModelAdmin):
#    fields = ['data', 'horario', 'reds']
    model = Evento
    list_display = ('reds', 'data', 'horario' )
    fieldsets = [
        (None,               {'fields': ['data', 'horario', 'reds']}),
        ('Detalhes', {'fields': ['is_disparo_via_publica','is_disparo_bpm','is_disparo_dpc','is_troca_de_tiros','is_encapuzados','is_colete_balistico','is_miguelitos_fuga']}),
        (None,               {'fields': ['TipoPenalCp', 'Bairro' ]}),
    ]

admin.site.register(Evento,EventoDetalhe)
admin.site.register(Bairro)
admin.site.register(TipoPenalCp)
admin.site.register(Cidade)


