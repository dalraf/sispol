# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from django.apps import AppConfig

# Register your models here.

from .models import *

admin.site.site_header = 'Sistema Policial'
admin.site.site_title = 'Sistema Policial'
admin.site.index_title = 'Sistema Policial'

class EventoDetalhe(admin.ModelAdmin):
#    fields = ['data', 'horario', 'reds']
    model = Evento
    list_display = ('reds', 'data', 'horario' )
    list_filter = (('data', DateRangeFilter ),)
    search_fields = ('reds',)
    fieldsets = [
        (None,{'fields': ['data', 'horario', 'reds']}),
        ('Detalhes', {'fields': ['is_disparo_via_publica','is_disparo_bpm','is_disparo_dpc','is_troca_de_tiros','is_encapuzados','is_colete_balistico','is_miguelitos_fuga']}),
        (None,{'fields': ['TipoPenalCp', 'Bairro' ]}),
    ]

class SuspeitoDetalhe(admin.ModelAdmin):
    #    fields = ['data', 'horario', 'reds']
    model = Suspeito
    list_display = ('nome', 'rg', 'data_nascimento' )
    list_filter = (('data_nascimento', DateRangeFilter ),)
    search_fields = ('nome',)
    fieldsets = [
        ('Dados Pessoais',{'fields': ['nome', 'alcunha', 'rg', 'cpf' ,'naturalidade', 'uf', 'data_nascimento','nome_da_mae','regiao','is_foto',]}),
        ('Dados Policiais', {'fields': ['fonte','ModusOperandi','TipoEnvolvimentoSuspeito','TipoSituacaoPrisional','data_ultima_prisao','UnidadePrisional','is_monitoramento_sige','is_alta_periculosidade', 'is_confronto_policia', 'id_faccao']}),
    ]

class VeiculoEventoInc(admin.TabularInline):
    model = VeiculoEvento
    extra = 1


class VeiculoDetalhe(admin.ModelAdmin):
    #    fields = ['data', 'horario', 'reds']
    model = Veiculo
    list_display = ('placa', 'nome','fabricante' )
    search_fields = ('placa','nome','fabricante',)
    inlines = [VeiculoEventoInc]

admin.site.register(Suspeito,SuspeitoDetalhe)
admin.site.register(Evento,EventoDetalhe)
admin.site.register(Bairro)
admin.site.register(TipoPenalCp)
admin.site.register(Cidade)
admin.site.register(Armamento)
admin.site.register(FabricanteArmamento)
admin.site.register(TipoArmamento)
admin.site.register(Faccao)
admin.site.register(Material)
admin.site.register(ModusOperandi)
admin.site.register(ObjetoAlvo)
admin.site.register(TipoSituacaoPrisional)
admin.site.register(UnidadePrisional)
admin.site.register(Veiculo,VeiculoDetalhe)
admin.site.register(TipoEnvolvimentoSuspeito)




