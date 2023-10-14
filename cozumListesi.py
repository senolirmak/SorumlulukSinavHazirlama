#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:31:15 2023

@author: senolirmak
"""
from src.sinavCozum import SinavProgramiUret
import pandas as pd


dataDersVeri_xls = "./data/2023/eylul/islenmis/2023_DersCikti_Eylül.xlsx"
dataDersKodu_xls ="./data/2023/eylul/islenmis/2023_Kod_Eylül.xlsx"

xlsxliste = SinavProgramiUret(dataDersVeri_xls, dataDersKodu_xls)


xcozum = [
    ['ders_4211', 'ders_0010', 'ders_1809', 'ders_5211', 'ders_3112', 'ders_2510', 'ders_2410'],
    ['ders_4709', 'ders_0309', 'ders_4111', 'ders_8811', 'ders_1910', 'ders_0710', 'ders_7010'],
    ['ders_3911', 'ders_0310', 'ders_0510', 'ders_2012', 'ders_2911', 'ders_2211', 'ders_1409'],
    ['ders_2811', 'ders_0509', 'ders_4910', 'ders_7211', 'ders_7812', 'ders_6611', 'ders_0112'],
    ['ders_6810', 'ders_6511', 'ders_1210', 'ders_1909', 'ders_4312', 'ders_1109', 'ders_7912'],
    ['ders_7112', 'ders_4809', 'ders_1511', 'ders_1009', 'ders_0009', 'ders_8211', 'ders_5812'],
    ['ders_8911', 'ders_4412', 'ders_5912', 'ders_4011', 'ders_1810', 'ders_2711', 'ders_7311'],
    ['ders_6311', 'ders_6910', 'ders_3611', 'ders_0709', 'ders_2511', 'ders_9010', 'ders_8411'],
    ['ders_9311', 'ders_0909', 'ders_1412', 'ders_8111', 'ders_0409', 'ders_1510', 'ders_9411'],
    ['ders_1309', 'ders_8311', 'ders_8011', 'ders_5611', 'ders_1410', 'ders_5111', 'ders_2209'],
    ['ders_4611', 'ders_5712', 'ders_8711', 'ders_8511', 'ders_6011', 'ders_3711', 'ders_0110'],
    ['ders_0609', 'ders_9211', 'ders_2612', 'ders_5411', 'ders_1710', 'ders_0809', 'ders_3312'],
    ['ders_6711', 'ders_1609', 'ders_7510', 'ders_3811', 'ders_5311', 'ders_5510', 'ders_0512'],
    ['ders_6211', 'ders_4511', 'ders_2110', 'ders_7611', 'ders_1411', 'ders_3011'],
    ['ders_3412', 'ders_8612', 'ders_7411', 'ders_1509', 'ders_0111'],
    ['ders_3210', 'ders_7711', 'ders_3512', 'ders_2011'],
    ['ders_5011', 'ders_6111', 'ders_1610', 'ders_0511'],
    ['ders_0209', 'ders_2010', 'ders_0810', 'ders_1709'],
    ['ders_9110', 'ders_6409', 'ders_2210', 'ders_2009'],
    ['ders_3211', 'ders_0109', 'ders_2310'],
    ]

sayfa=list()
for veri in xcozum:
    #coz1Dersler = [getDersAdi(x) for x in coz1]
    f = dict()
    for a in veri:
        y = xlsxliste.sinavOturumDersAyrintili(a)
        f = y.copy()
        sayfa.append(f)
        y.clear()


data = pd.DataFrame(sayfa)
data.to_excel("SınavProgramı_2023_Eylül.xlsx", index=False) 