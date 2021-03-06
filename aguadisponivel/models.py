from django.db import models
import os.path
import sqlite3
# Create your models here.



class PTFdados(models.Model):
    #id_emb = models.CharField(max_length=50, null= True)
    SBICS = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name='Classificação nova SBICS')
    OLD = models.CharField(max_length=200, null=True,
                           blank=True,  verbose_name='Classificação antiga')
    LAT = models.FloatField(null=True, blank=True,  verbose_name='Latitude')
    LON = models.FloatField(null=True, blank=True, verbose_name='Longitude')
    MUN = models.CharField(max_length=60, null=True,
                           blank=True, verbose_name='Municipio')
    GEOCOD = models.IntegerField(
        null=True, blank=True, verbose_name="codigo do municipio IBGE")
    T_ARE = models.FloatField(null=True, blank=True,
                              verbose_name='Total de areia* em g/kg')
    AGRO = models.FloatField(
        null=True, blank=True, verbose_name='Total de areia grossa (2 - 0,2 mm) em g/kg')
    AFIN = models.FloatField(
        null=True, blank=True, verbose_name='Total de areia Fina (0,2 - 0,05 mm) em g/kg')
    SILT = models.FloatField(
        null=True, blank=True, verbose_name='Total de Silte (0,05 - 0,002 mm) em g/kg')
    ARG = models.FloatField(null=True, blank=True,
                            verbose_name='Total de Argila (< 0,002 mm) em g/kg')
    SOLO = models.FloatField(null=True, blank=True,
                             verbose_name='Densidade do Solo em g/dm³')
    C_ORG = models.FloatField(null=True, blank=True,
                              verbose_name='Total Carbono Orgânico* em g/kg')
    M_ORG = models.FloatField(null=True, blank=True)
    OLIV = models.FloatField(null=True, blank=True)
    B_ZU = models.FloatField(null=True, blank=True)
    B_TT = models.FloatField(null=True, blank=True,
                             verbose_name='Theta a 33mm')
    B_PC = models.FloatField(null=True, blank=True,
                             verbose_name='Theta a 1500mm')
    B_ALPHA = models.FloatField(null=True, blank=True)
    B_N = models.FloatField(null=True, blank=True)
    B_THETAS = models.FloatField(null=True, blank=True)
    B_TETHAR = models.FloatField(null=True, blank=True)
    B_AD = models.FloatField(null=True, blank=True)
    T_ZU = models.FloatField(null=True, blank=True)
    T_TT = models.FloatField(null=True, blank=True)
    T_PC = models.FloatField(null=True, blank=True)
    T_ALPHA = models.FloatField(null=True, blank=True)
    T_N = models.FloatField(null=True, blank=True)
    T_THETAR = models.FloatField(null=True, blank=True)
    T_TETHAS = models.FloatField(null=True, blank=True)
    T_AD = models.FloatField(null=True, blank=True)
    ct = 'ct'
    asa = 'asa'
    asad = 'asad'
    asadtt = 'asadtt'
    asadpc = 'asadpc'
    opcoes = [
        (ct, 'Classes Texturais'),
        (asa, 'Areia, silte e argila'),
        (asad, 'Areia, silte e argila e densidade'),
        (asadtt, 'Areia, Silt, Argila, Densidade e AD 33kPa (TH33)'),
        (asadpc, 'Areia, Silt, Argila e Densidade e AD 1500kPa (TH1500)'),
    ]
    escolha = models.CharField(max_length=300, choices=opcoes, verbose_name="escolha uma opção de calculo:", null=True, blank=True)

    # soma de areia, silt, argila tem que dar 100
    # densidade 2>= d >= 0,8
    # campos densidae, silt, argila, areia tem q ser preenchidos

    def __str__(self):
        return id
