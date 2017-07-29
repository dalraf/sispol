# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Alvo(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    TipoAlvo = models.ForeignKey('TipoAlvo', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'ALVO'


class AlvoEvento(models.Model):
    Alvo = models.ForeignKey(Alvo, on_delete=models.CASCADE )
    Evento = models.ForeignKey('Evento', on_delete=models.CASCADE )
    is_consumado = models.IntegerField()
    ModusOperandi = models.ForeignKey('ModusOperandi', on_delete=models.CASCADE )
    ObjetoAlvo = models.ForeignKey('ObjetoAlvo', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ALVO_EVENTO'
        unique_together = (('Alvo', 'Evento'),)


class Armamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    is_artesanal = models.IntegerField(blank=True, null=True)
    calibre = models.CharField(max_length=10, blank=True, null=True)
    numeracao = models.CharField(max_length=10, blank=True, null=True)
    FabricanteArmamento = models.ForeignKey('FabricanteArmamento', on_delete=models.CASCADE )
    TipoArmamento = models.ForeignKey('TipoArmamento', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'ARMAMENTO'


class ArmamentoEvento(models.Model):
    Armamento = models.ForeignKey(Armamento, on_delete=models.CASCADE )
    Evento = models.ForeignKey('Evento', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'ARMAMENTO_EVENTO'
        unique_together = (('Armamento', 'Evento'),)


class Bairro(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    CidadeMg = models.ForeignKey('CidadeMg', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'BAIRRO'


class CidadeMg(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    num_habitantes = models.IntegerField(blank=True, null=True)
    latidude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    dpc_destinataria = models.CharField(max_length=100, blank=True, null=True)
    regional_pcmg = models.CharField(max_length=10, blank=True, null=True)
    departamento_pcmg = models.CharField(max_length=10, blank=True, null=True)
    uf_fronteira = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CIDADE_MG'


class Comparsas(models.Model):
    SuspeitoPrimario = models.ForeignKey('Suspeito', on_delete=models.CASCADE , related_name="SuspeitoPrimario" )
    SuspeitoSecundario = models.ForeignKey('Suspeito', on_delete=models.CASCADE, related_name="SuspeitoSecundario")

    class Meta:
        managed = True
        db_table = 'COMPARSAS'
        unique_together = (('SuspeitoPrimario', 'SuspeitoSecundario'),)


class Evento(models.Model):
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
    TipoPenalCp = models.ForeignKey('TipoPenalCp', on_delete=models.CASCADE )
    id_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE )
    id_cidade = models.ForeignKey(CidadeMg, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'EVENTO'


class FabricanteArmamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FABRICANTE_ARMAMENTO'


class Faccao(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FACCAO'


class Material(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)
    is_venda_controlada = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MATERIAL'


class MaterialEvento(models.Model):
    Material = models.ForeignKey(Material, on_delete=models.CASCADE )
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'MATERIAL_EVENTO'
        unique_together = (('Material', 'Evento'),)


class ModusOperandi(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MODUS_OPERANDI'


class ObjetoAlvo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'OBJETO_ALVO'


class SupeitoCrimes(models.Model):
    TipoPenalCp = models.ForeignKey('TipoPenalCp', on_delete=models.CASCADE )
    Suspeito = models.ForeignKey('Suspeito', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'SUPEITO_CRIMES'
        unique_together = (('TipoPenalCp', 'Suspeito'),)


class Suspeito(models.Model):
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
    id_modus_operandi = models.ForeignKey(ModusOperandi, on_delete=models.CASCADE )
    TipoEnvolvimentoSuspeito = models.ForeignKey('TipoEnvolvimentoSuspeito', on_delete=models.CASCADE )
    TipoSituacaoPrisional = models.ForeignKey('TipoSituacaoPrisional', on_delete=models.CASCADE )
    data_ultima_prisao = models.DateField(blank=True, null=True)
    UnidadePrisional = models.ForeignKey('UnidadePrisional', on_delete=models.CASCADE )
    is_monitoramento_sige = models.IntegerField(blank=True, null=True)
    is_alta_periculosidade = models.IntegerField(blank=True, null=True)
    is_confronto_policia = models.IntegerField(blank=True, null=True)
    id_faccao = models.ForeignKey(Faccao, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'SUSPEITO'


class SuspeitoAlvo(models.Model):
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )
    Suspeito = models.ForeignKey(Suspeito, on_delete=models.CASCADE )
    data_inclusao = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SUSPEITO_ALVO'
        unique_together = (('Evento', 'Suspeito'),)


class SuspeitoCidade(models.Model):
    CidadeMg = models.ForeignKey(CidadeMg, on_delete=models.CASCADE )
    Suspeito = models.ForeignKey(Suspeito, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'SUSPEITO_CIDADE'
        unique_together = (('CidadeMg', 'Suspeito'),)


class SuspeitoEventos(models.Model):
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )
    Suspeito = models.ForeignKey(Suspeito, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'SUSPEITO_EVENTOS'
        unique_together = (('Evento', 'Suspeito'),)


class TipoAlvo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TIPO_ALVO'


class TipoArmamento(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TIPO_ARMAMENTO'


class TipoEnvolvimentoSuspeito(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TIPO_ENVOLVIMENTO_SUSPEITO'


class TipoPenalCp(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    art = models.IntegerField(blank=True, null=True)
    paragrafo = models.CharField(max_length=10, blank=True, null=True)
    inciso = models.CharField(max_length=10, blank=True, null=True)
    alinea = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TIPO_PENAL_CP'


class TipoSituacaoPrisional(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TIPO_SITUACAO_PRISIONAL'


class UnidadePrisional(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'UNIDADE_PRISIONAL'


class Veiculo(models.Model):
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
        managed = True
        db_table = 'VEICULO'


class VeiculoEvento(models.Model):
    Veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE )
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'VEICULO_EVENTO'
        unique_together = (('Veiculo', 'Evento'),)
