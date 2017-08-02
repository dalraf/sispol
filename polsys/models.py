# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.safestring import mark_safe

class Alvo(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    TipoAlvo = models.ForeignKey('TipoAlvo', on_delete=models.CASCADE )
    
    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'ALVO'


class AlvoEvento(models.Model):
    Alvo = models.ForeignKey(Alvo, on_delete=models.CASCADE )
    Evento = models.ForeignKey('Evento', on_delete=models.CASCADE )
    Consumado = models.BooleanField()
    ModusOperandi = models.ForeignKey('ModusOperandi', verbose_name = 'Modus Operandi', on_delete=models.CASCADE )
    ObjetoAlvo = models.ForeignKey('ObjetoAlvo', verbose_name = 'Objeto Alvo', on_delete=models.CASCADE, blank=True, null=True)
    
    def __unicode__(self):
        return self.Alvo.nome

    class Meta:
        managed = True
        db_table = 'ALVO_EVENTO'
        unique_together = (('Alvo', 'Evento'),)
        verbose_name = 'Alvo Eventos'
        verbose_name_plural = 'Alvos Eventos'


class Armamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    is_artesanal = models.BooleanField("Arsenal")
    calibre = models.CharField(max_length=10, blank=True, null=True)
    numeracao = models.CharField(max_length=10, blank=True, null=True)
    FabricanteArmamento = models.ForeignKey('FabricanteArmamento', verbose_name = 'Fabricante do Armamento', on_delete=models.CASCADE )
    TipoArmamento = models.ForeignKey('TipoArmamento', verbose_name = 'Tipo de Armamento', on_delete=models.CASCADE )

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'ARMAMENTO'


class ArmamentoEvento(models.Model):
    Armamento = models.ForeignKey('Armamento', on_delete=models.CASCADE )
    Evento = models.ForeignKey('Evento', on_delete=models.CASCADE )

    def __unicode__(self):
        return self.Armamento.nome + ' / ' + self.Evento.reds

    class Meta:
        managed = True
        db_table = 'ARMAMENTO_EVENTO'
        unique_together = (('Armamento', 'Evento'),)
        verbose_name = 'Armamento Evento'
        verbose_name_plural = 'Armamentos Eventos'


class Bairro(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    Cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE )

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'BAIRRO'


class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    num_habitantes = models.IntegerField(blank=True, null=True)
    latidude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    dpc_destinataria = models.CharField(max_length=100, blank=True, null=True)
    regional_pcmg = models.CharField(max_length=10, blank=True, null=True)
    departamento_pcmg = models.CharField(max_length=10, blank=True, null=True)
    uf_fronteira = models.CharField(max_length=2, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'CIDADE_MG'


class Comparsas(models.Model):
    SuspeitoPrimario = models.ForeignKey('Suspeito', on_delete=models.CASCADE , verbose_name = 'Suspeito Primário', related_name="SuspeitoPrimario" )
    SuspeitoSecundario = models.ForeignKey('Suspeito', on_delete=models.CASCADE, verbose_name = 'Suspeito Secundario', related_name="SuspeitoSecundario")

    def __unicode__(self):
        return self.SuspeitosSecundario.nome

    class Meta:
        managed = True
        db_table = 'COMPARSAS'
        unique_together = (('SuspeitoPrimario', 'SuspeitoSecundario'),)
        verbose_name = 'Comparsa'
        verbose_name_plural = 'Comparsas'


class Evento(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    reds = models.CharField(max_length=19)
    is_disparo_via_publica = models.IntegerField('Disparos em via públicas', blank=True, null=True)
    is_disparo_bpm = models.BooleanField('Disparo BPM')
    is_disparo_dpc = models.BooleanField('Disparo DPC')
    is_troca_de_tiros = models.BooleanField('Troca de Tiros')
    is_encapuzados = models.BooleanField('Encapuzados')
    is_colete_balistico = models.BooleanField('Colete Balístico')
    is_miguelitos_fuga = models.BooleanField('Miguelitos Fuga')
    Crime = models.ForeignKey('Crime',verbose_name="Crime",on_delete=models.CASCADE )
    ValorSubtraido = models.DecimalField('Valor Subtraído (R$)',blank=True, null=True, max_digits=8, decimal_places=2 )
    MassaSubtraida = models.DecimalField('Quantidade Subtraída (Kg)', blank=True, null=True,max_digits=10, decimal_places=3)
    Bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE )

    def __unicode__(self):
        return self.reds

 
    class Meta:
        managed = True
        db_table = 'EVENTO'


class FabricanteArmamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'FABRICANTE_ARMAMENTO'
        verbose_name = 'Fabricante do Armamento'
        verbose_name_plural = 'Fabricantes de Armamento'


class Faccao(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'FACCAO'
        verbose_name = 'Facção'
        verbose_name_plural = 'Facções'



class Material(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)
    is_venda_controlada = models.BooleanField('Venda Controlada')

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'MATERIAL'
        verbose_name_plural = 'Materiais'


class MaterialEvento(models.Model):
    Material = models.ForeignKey(Material, on_delete=models.CASCADE )
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )

    def __unicode__(self):
        return self.Material.nome

    class Meta:
        managed = True
        db_table = 'MATERIAL_EVENTO'
        unique_together = (('Material', 'Evento'),)
        verbose_name = 'Material Evento'
        verbose_name_plural = 'Materiais Eventos'


class ModusOperandi(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'MODUS_OPERANDI'
        verbose_name = 'Modus Operandis'
        verbose_name_plural = 'Modi Operandi'


class ObjetoAlvo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'OBJETO_ALVO'
        verbose_name = 'Objeto Alvo'
        verbose_name_plural = 'Objetos Alvo'


class SupeitoCrimes(models.Model):
    Crime = models.ForeignKey('Crime', verbose_name = 'Crime', on_delete=models.CASCADE )
    Suspeito = models.ForeignKey('Suspeito', on_delete=models.CASCADE )

    def __unicode__(self):
        return self.Crime.nome

    class Meta:
        managed = True
        db_table = 'SUPEITO_CRIMES'
        unique_together = (('Crime', 'Suspeito'),)
        verbose_name = 'Suspeito Crime'
        verbose_name_plural = 'Suspeitos Crimes'


class Suspeito(models.Model):
    nome = models.CharField(max_length=100,)
    alcunha = models.CharField(max_length=200,)
    rg = models.CharField('RG',max_length=10,)
    cpf = models.DecimalField('CPF',max_digits=10, decimal_places=0,)
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField('CPF',max_length=2, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento',blank=True, null=True)
    nome_da_mae = models.CharField('Nome da mãe',max_length=100, blank=True, null=True)
    infopen = models.IntegerField('INFOPEN',blank=True, null=True)
    regiao = models.CharField('Região',max_length=100, blank=True, null=True)
    is_foto = models.BooleanField('Foto')
    foto = models.ImageField('Foto Arquivo',upload_to='fotosuspeito', null=True)
    fonte = models.CharField(max_length=50, blank=True, null=True)
    ModusOperandi = models.ForeignKey(ModusOperandi, verbose_name='Modus Operandi', on_delete=models.CASCADE )
    TipoEnvolvimentoSuspeito = models.ForeignKey('TipoEnvolvimentoSuspeito', verbose_name='Tipo de envolvimento do Suspeito' , on_delete=models.CASCADE )
    TipoSituacaoPrisional = models.ForeignKey('TipoSituacaoPrisional', verbose_name='Tipo de situação prisional', on_delete=models.CASCADE )
    data_ultima_prisao = models.DateField('Data da última prisão',blank=True, null=True)
    UnidadePrisional = models.ForeignKey('UnidadePrisional', verbose_name='Unidade Prisional', on_delete=models.CASCADE )
    is_monitoramento_sige = models.BooleanField('Monitoramento Sige')
    is_alta_periculosidade = models.BooleanField('Alta periculosidade')
    is_confronto_policia = models.BooleanField('Confronto polícia')
    id_faccao = models.ForeignKey(Faccao, verbose_name='Facção', on_delete=models.CASCADE )

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.foto))
    image_tag.short_description = 'Imagem'

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'SUSPEITO'


class SuspeitoAlvo(models.Model):
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE )
    Suspeito = models.ForeignKey(Suspeito, on_delete=models.CASCADE )
    data_inclusao = models.DateField('Data da Inclusão',blank=True, null=True)

    def __unicode__(self):
        return self.Evento.reds + ' / ' +  str(self.data_inclusao)

    class Meta:
        managed = True
        db_table = 'SUSPEITO_ALVO'
        unique_together = (('Evento', 'Suspeito'),)
        verbose_name = 'Suspeito Alvo'
        verbose_name_plural = 'Suspeitos Alvos'


class SuspeitoCidade(models.Model):
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE )
    Suspeito = models.ForeignKey(Suspeito, on_delete=models.CASCADE )

    def __unicode__(self):
        return self.Cidade.nome

    class Meta:
        managed = True
        db_table = 'SUSPEITO_CIDADE'
        unique_together = (('Cidade', 'Suspeito'),)


class TipoAlvo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'TIPO_ALVO'
        verbose_name = 'Tipo de Alvo'
        verbose_name_plural = 'Tipos de Alvo'


class TipoArmamento(models.Model):
    nome = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'TIPO_ARMAMENTO'
        verbose_name = 'Tipo de Armamento'
        verbose_name_plural = 'Tipos de Armamento'


class TipoEnvolvimentoSuspeito(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'TIPO_ENVOLVIMENTO_SUSPEITO'
        verbose_name = 'Tipo de envolvimento de Suspeito'
        verbose_name_plural = 'Tipos de envolvimento de Suspeito'


class Crime(models.Model):
    nome = models.CharField('Crime',max_length=50, blank=True, null=True)
    art = models.DecimalField(max_digits=10, decimal_places=0)
    paragrafo = models.CharField(max_length=10, blank=True, null=True)
    inciso = models.CharField(max_length=10, blank=True, null=True)
    alinea = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'TIPO_CrimeL_CP'
        verbose_name = "Crime"


class TipoSituacaoPrisional(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'TIPO_SITUACAO_PRISIONAL'
        verbose_name = 'Tipo de Situação Prisional'
        verbose_name_plural = 'Tipos de Situação Prisional'


class UnidadePrisional(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'UNIDADE_PRISIONAL'
        verbose_name = 'Unidade Prisional'
        verbose_name_plural = 'Unidades Prisionais'


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, blank=True, null=True)
    nome = models.CharField(max_length=10, blank=True, null=True)
    fabricante = models.CharField(max_length=10, blank=True, null=True)
    is_caminhonete = models.BooleanField('Caminhonete')
    is_importado = models.BooleanField('Importado')
    is_moto = models.BooleanField('Moto')
    is_clonado = models.BooleanField('Clonado')
    is_roubado_furtado = models.BooleanField('Roubado/Furtado')
    is_alugado = models.BooleanField('Alugado')
    cpf_proprietario = models.IntegerField('CPF do proprietário',blank=True, null=True)


    def __unicode__(self):
        return self.placa + ' / ' + self.nome + ' / ' + self.fabricante

    class Meta:
        managed = True
        db_table = 'VEICULO'
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'


class VeiculoEvento(models.Model):
    Veiculo = models.ForeignKey(Veiculo, verbose_name = 'Veículos' , on_delete=models.CASCADE )
    Evento = models.ForeignKey(Evento, verbose_name = 'Evento' , on_delete=models.CASCADE )

    def __unicode__(self):
        return self.Veiculo.nome

    class Meta:
        managed = True
        db_table = 'VEICULO_EVENTO'
        unique_together = (('Veiculo', 'Evento'),)
        verbose_name = 'Veículo em evento'
        verbose_name_plural = 'Veículos em eventos'
