#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:23:13 2023

@author: senolirmak
"""
from src.ogrenciSinavTakvimi import simple_table

from src.sinavCozum import SinavProgramiUret
import pandas as pd


# gereksiz uyarıları kapatalım
import warnings
warnings.filterwarnings('ignore')

dataDers = "./data/2023/eylul/islenmis/2023_DersCikti_Eylül.xlsx"
dersKodu = "./data/2023/eylul/islenmis/2023_Kod_Eylül.xlsx"

verilerODS = "./data/2023/eylul/program/Eylül_2023_Sorumluluk_07Eylul.ods"
verilerODS_sheet="Asilacak"


program = SinavProgramiUret(dataDers, dersKodu)


neworenciT = program.sinavTakvimiOgrenciler(verilerODS, verilerODS_sheet) #pd.read_excel("xxData.xlsx")
_ , okulnoArry = pd.factorize(neworenciT['okulno'])

okulnoList = okulnoArry.tolist()
path = "./data/2023/ogrenci/"

def ogrenciSınavTakvimi(okulno):

    nquery = neworenciT.query("okulno == "+okulno)
    nquery_adix = nquery [['okulno', 'adisoyadi','sinifalan']]
    nquery_adix = nquery_adix.drop_duplicates(subset=['okulno'])
    nquery_sinvx = nquery[['tarih', 'saat', 'duzey','ders', 'yer']]
    nquery_sinvx = nquery_sinvx.sort_values(by=['tarih','saat'], ascending=True)
    adix_data=list(nquery_adix.itertuples(index=False, name=None))
    sinvx_data=list(nquery_sinvx.itertuples(index=False, name=None))

    OkulNo = "Okul No: "+str(okulno)

    simple_table(sinvx_data,adix_data,path,OkulNo)


sayac = 0

while True:
    y = input("Okul Numarasını Giriniz: ")
    y = int(y)
    if y in okulnoList:
       ogrenciSınavTakvimi(str(y))
       sayac = 3
   
    elif y == -1:
        break
    else:
       print("Sorumluk Sınav Listesinde öğrenci yok veya numara hatalı")
       #sayac +=1

    