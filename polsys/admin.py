# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from jet.filters import DateRangeFilter

from django.apps import AppConfig

# Register your models here.

from .models import *

admin.site.site_header = 'Sistema Policial'
admin.site.site_title = 'Sistema Policial'
admin.site.index_title = 'Sistema Policial'

class VeiculoEventoInc(admin.TabularInline):
#    raw_id_fields = ('Veiculo',)
    model = VeiculoEvento
    extra = 0

class SuspeitoAlvoInc(admin.TabularInline):
#    raw_id_fields = ('Suspeito','Evento',)
    model = SuspeitoAlvo
    extra = 0

class SuspeitoCrimesInc(admin.TabularInline):
#    raw_id_fields = ('Crime',)
    model = SupeitoCrimes
    extra = 0

class MaterialEventoInc(admin.TabularInline):
 #   raw_id_fields = ('Material',)
    model = MaterialEvento
    extra = 0

class ArmamentoEventoInc(admin.TabularInline):
#    raw_id_fields = ('Armamento',)
    model = ArmamentoEvento
    extra = 0

class AlvoEventoInc(admin.TabularInline):
#    raw_id_fields = ('Alvo','ModusOperandi','ObjetoAlvo')
    model = AlvoEvento
    extra = 0

class EventoDetalhe(admin.ModelAdmin):
    model = Evento
    list_display = ('reds', 'data', 'horario' )
    list_filter = (('data', DateRangeFilter ),)
    search_fields = ('reds',)
    inlines = [SuspeitoAlvoInc,VeiculoEventoInc,MaterialEventoInc,ArmamentoEventoInc,AlvoEventoInc]
    readonly_fields = ('diadasemana',)
 #   raw_id_fields = ('Crime','Bairro',)
    fieldsets = [
        ('Dados',{'fields': ['data', 'horario', 'diadasemana', 'reds']}),
        ('Detalhes', {'fields': ['is_disparo_via_publica','is_disparo_bpm','is_disparo_dpc','is_troca_de_tiros','is_encapuzados','is_colete_balistico','is_miguelitos_fuga','ValorSubtraido', 'MassaSubtraida',]}),
        ('Adicionais',{'fields': ['Crime', 'Bairro','Fronteira','informacoescomplementares' ]}),
    ]

class SuspeitoDetalhe(admin.ModelAdmin):
    model = Suspeito
    list_display = ('nome', 'rg', 'data_nascimento' )
    list_filter = (('data_nascimento', DateRangeFilter ),)
    filter_horizontal = ('Comparsas',)
    inlines = [SuspeitoAlvoInc,SuspeitoCrimesInc]
    search_fields = ('nome',)
    readonly_fields = ('image_tag',)
#    raw_id_fields = ('ModusOperandi','TipoEnvolvimentoSuspeito','TipoSituacaoPrisional','UnidadePrisional','id_faccao')
    fieldsets = [
        ('Dados Pessoais',{'fields': ['nome', 'alcunha', 'rg', 'cpf' ,'naturalidade', 'uf', 'data_nascimento','nome_da_mae','regiao','is_foto','foto','image_tag',]}),
        ('Dados Policiais', {'fields': ['fonte','ModusOperandi','TipoEnvolvimentoSuspeito','TipoSituacaoPrisional','data_ultima_prisao','UnidadePrisional','is_monitoramento_sige','is_alta_periculosidade', 'is_confronto_policia', 'id_faccao','Comparsas']}),
    ]
class VeiculoDetalhe(admin.ModelAdmin):
    model = Veiculo
    list_display = ('placa', 'nome','fabricante' )
    search_fields = ('placa','nome','fabricante',)
    inlines = [VeiculoEventoInc]

admin.site.register(Suspeito,SuspeitoDetalhe)
admin.site.register(Evento,EventoDetalhe)
admin.site.register(Veiculo,VeiculoDetalhe)

class BairroDetalhe(admin.ModelAdmin):
    model = Bairro
#    raw_id_fields = ('Cidade',)

admin.site.register(Bairro,BairroDetalhe)

class ArmamentoDetalhe(admin.ModelAdmin):
    model = Armamento
#    raw_id_fields = ('FabricanteArmamento','TipoArmamento')

admin.site.register(Armamento,ArmamentoDetalhe)

admin.site.register(Crime)
admin.site.register(Cidade)
admin.site.register(FabricanteArmamento)
admin.site.register(TipoArmamento)
admin.site.register(Faccao)
admin.site.register(Material)
admin.site.register(ModusOperandi)
admin.site.register(ObjetoAlvo)
admin.site.register(TipoSituacaoPrisional)
admin.site.register(UnidadePrisional)
admin.site.register(TipoEnvolvimentoSuspeito)
admin.site.register(TipoAlvo)
admin.site.register(Alvo)




