# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Alvo(models.Model):
    id_alvo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    id_tipo_alvo = models.ForeignKey('TipoAlvo', models.DO_NOTHING, db_column='id_tipo_alvo')

    class Meta:
        managed = False
        db_table = 'ALVO'


class AlvoEvento(models.Model):
    id_alvo = models.ForeignKey(Alvo, models.DO_NOTHING, db_column='id_alvo', primary_key=True)
    id_evento = models.ForeignKey('Evento', models.DO_NOTHING, db_column='id_evento')
    is_consumado = models.IntegerField()
    id_modus_operandi = models.ForeignKey('ModusOperandi', models.DO_NOTHING, db_column='id_modus_operandi')
    id_objeto_alvo = models.ForeignKey('ObjetoAlvo', models.DO_NOTHING, db_column='id_objeto_alvo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ALVO_EVENTO'
        unique_together = (('id_alvo', 'id_evento'),)


class Armamento(models.Model):
    id_armamento = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    is_artesanal = models.IntegerField(blank=True, null=True)
    calibre = models.CharField(max_length=10, blank=True, null=True)
    numeracao = models.CharField(max_length=10, blank=True, null=True)
    id_fabricante_armamento = models.ForeignKey('FabricanteArmamento', models.DO_NOTHING, db_column='id_fabricante_armamento')
    id_tipo_armamento = models.ForeignKey('TipoArmamento', models.DO_NOTHING, db_column='id_tipo_armamento')

    class Meta:
        managed = False
        db_table = 'ARMAMENTO'


class ArmamentoEvento(models.Model):
    id_armamento = models.ForeignKey(Armamento, models.DO_NOTHING, db_column='id_armamento', primary_key=True)
    id_evento = models.ForeignKey('Evento', models.DO_NOTHING, db_column='id_evento')

    class Meta:
        managed = False
        db_table = 'ARMAMENTO_EVENTO'
        unique_together = (('id_armamento', 'id_evento'),)


class Bairro(models.Model):
    id_bairro = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    id_cidade = models.ForeignKey('CidadeMg', models.DO_NOTHING, db_column='id_cidade')

    class Meta:
        managed = False
        db_table = 'BAIRRO'


class CidadeMg(models.Model):
    id_cidade = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    num_habitantes = models.IntegerField(blank=True, null=True)
    latidude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    dpc_destinataria = models.CharField(max_length=100, blank=True, null=True)
    regional_pcmg = models.CharField(max_length=10, blank=True, null=True)
    departamento_pcmg = models.CharField(max_length=10, blank=True, null=True)
    uf_fronteira = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CIDADE_MG'


class Comparsas(models.Model):
    id_suspeito = models.ForeignKey('Suspeito', models.DO_NOTHING, db_column='id_suspeito', primary_key=True)
    id_suspeito_0 = models.ForeignKey('Suspeito', models.DO_NOTHING, db_column='id_suspeito_0')

    class Meta:
        managed = False
        db_table = 'COMPARSAS'
        unique_together = (('id_suspeito', 'id_suspeito_0'),)


class Evento(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    reds = models.CharField(max_length=19, blank=True, null=True)
    is_disparo_via_publica = models.IntegerField()
    is_disparo_bpm = models.IntegerField(blank=True, null=True)
    is_disparo_dpc = models.IntegerField(blank=True, null=True)
    is_troca_de_tiros = models.IntegerField(blank=True, null=True)
    is_encapuzados = models.IntegerField(blank=True, null=True)
    is_colete_balistico = models.CharField(max_length=10, blank=True, null=True)
    is_miguelitos_fuga = models.CharField(max_length=10, blank=True, null=True)
    id_tipo_penal = models.ForeignKey('TipoPenalCp', models.DO_NOTHING, db_column='id_tipo_penal')
    id_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='id_bairro')
    id_cidade = models.ForeignKey(CidadeMg, models.DO_NOTHING, db_column='id_cidade')

    class Meta:
        managed = False
        db_table = 'EVENTO'


class FabricanteArmamento(models.Model):
    id_fabricante_armamento = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FABRICANTE_ARMAMENTO'


class Faccao(models.Model):
    id_faccao = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FACCAO'


class Material(models.Model):
    id_material = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=10, blank=True, null=True)
    is_venda_controlada = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MATERIAL'


class MaterialEvento(models.Model):
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='id_material', primary_key=True)
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento')

    class Meta:
        managed = False
        db_table = 'MATERIAL_EVENTO'
        unique_together = (('id_material', 'id_evento'),)


class ModusOperandi(models.Model):
    id_modus_operandi = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MODUS_OPERANDI'


class ObjetoAlvo(models.Model):
    id_objeto_alvo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OBJETO_ALVO'


class SupeitoCrimes(models.Model):
    id_tipo_penal = models.ForeignKey('TipoPenalCp', models.DO_NOTHING, db_column='id_tipo_penal', primary_key=True)
    id_suspeito = models.ForeignKey('Suspeito', models.DO_NOTHING, db_column='id_suspeito')

    class Meta:
        managed = False
        db_table = 'SUPEITO_CRIMES'
        unique_together = (('id_tipo_penal', 'id_suspeito'),)


class Suspeito(models.Model):
    id_suspeito = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    alcunha = models.CharField(max_length=200, blank=True, null=True)
    rg = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cpf = models.IntegerField(blank=True, null=True)
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    nome_da_mae = models.CharField(max_length=100, blank=True, null=True)
    infopen = models.IntegerField(blank=True, null=True)
    regiao = models.CharField(max_length=100, blank=True, null=True)
    is_foto = models.IntegerField(blank=True, null=True)
    fonte = models.CharField(max_length=50, blank=True, null=True)
    id_modus_operandi = models.ForeignKey(ModusOperandi, models.DO_NOTHING, db_column='id_modus_operandi')
    id_tipo_envolvimento_suspeito = models.ForeignKey('TipoEnvolvimentoSuspeito', models.DO_NOTHING, db_column='id_tipo_envolvimento_suspeito')
    id_tipo_situacao_prisional = models.ForeignKey('TipoSituacaoPrisional', models.DO_NOTHING, db_column='id_tipo_situacao_prisional')
    data_ultima_prisao = models.DateField(blank=True, null=True)
    id_unidade_prisional = models.ForeignKey('UnidadePrisional', models.DO_NOTHING, db_column='id_unidade_prisional')
    is_monitoramento_sige = models.IntegerField(blank=True, null=True)
    is_alta_periculosidade = models.IntegerField(blank=True, null=True)
    is_confronto_policia = models.IntegerField(blank=True, null=True)
    id_faccao = models.ForeignKey(Faccao, models.DO_NOTHING, db_column='id_faccao')

    class Meta:
        managed = False
        db_table = 'SUSPEITO'


class SuspeitoAlvo(models.Model):
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento', primary_key=True)
    id_suspeito = models.ForeignKey(Suspeito, models.DO_NOTHING, db_column='id_suspeito')
    data_inclusao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SUSPEITO_ALVO'
        unique_together = (('id_evento', 'id_suspeito'),)


class SuspeitoCidade(models.Model):
    id_cidade = models.ForeignKey(CidadeMg, models.DO_NOTHING, db_column='id_cidade', primary_key=True)
    id_suspeito = models.ForeignKey(Suspeito, models.DO_NOTHING, db_column='id_suspeito')

    class Meta:
        managed = False
        db_table = 'SUSPEITO_CIDADE'
        unique_together = (('id_cidade', 'id_suspeito'),)


class SuspeitoEventos(models.Model):
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento', primary_key=True)
    id_suspeito = models.ForeignKey(Suspeito, models.DO_NOTHING, db_column='id_suspeito')

    class Meta:
        managed = False
        db_table = 'SUSPEITO_EVENTOS'
        unique_together = (('id_evento', 'id_suspeito'),)


class TipoAlvo(models.Model):
    id_tipo_alvo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_ALVO'


class TipoArmamento(models.Model):
    id_tipo_armamento = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_ARMAMENTO'


class TipoEnvolvimentoSuspeito(models.Model):
    id_tipo_envolvimento_suspeito = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_ENVOLVIMENTO_SUSPEITO'


class TipoPenalCp(models.Model):
    id_tipo_penal = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    art = models.IntegerField(blank=True, null=True)
    paragrafo = models.CharField(max_length=10, blank=True, null=True)
    inciso = models.CharField(max_length=10, blank=True, null=True)
    alinea = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_PENAL_CP'


class TipoSituacaoPrisional(models.Model):
    id_tipo_situacao_prisional = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_SITUACAO_PRISIONAL'


class UnidadePrisional(models.Model):
    id_unidade_prisional = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UNIDADE_PRISIONAL'


class Veiculo(models.Model):
    id_veiculo = models.CharField(primary_key=True, max_length=10)
    placa = models.CharField(max_length=10, blank=True, null=True)
    nome = models.CharField(max_length=10, blank=True, null=True)
    fabricante = models.CharField(max_length=10, blank=True, null=True)
    is_caminhonete = models.CharField(max_length=10, blank=True, null=True)
    is_importado = models.CharField(max_length=10, blank=True, null=True)
    is_moto = models.CharField(max_length=10, blank=True, null=True)
    is_clonado = models.CharField(max_length=10, blank=True, null=True)
    is_roubado_furtado = models.CharField(max_length=10, blank=True, null=True)
    is_alugado = models.CharField(max_length=10, blank=True, null=True)
    cpf_proprietario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VEICULO'


class VeiculoEvento(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, models.DO_NOTHING, db_column='id_veiculo', primary_key=True)
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento')

    class Meta:
        managed = False
        db_table = 'VEICULO_EVENTO'
        unique_together = (('id_veiculo', 'id_evento'),)