#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:34:22 2023

@author: senolirmak
"""

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
saatler = ['13:00','14:00','15:00','16:00']
tarihler = ['18.09.2023', '19.09.2023','20.09.2023', '21.09.2023','22.09.2023']
path = "./data/2023/eylul/oturum/"
df = pd.DataFrame(columns=['okulno','adisoyadi',	'duzey',	'ders',	'tarih',	'saat','yer'	,'sinifalan'])

for tarih in tarihler:
    for saat in saatler:
        print(saat, tarih)
        neworenciToturum1 = neworenciT.query("tarih == '"+tarih+"' and saat == '"+saat+"'")
        #okulnoList = okulnoArry.tolist()
        #neworenciToturum1.to_excel("OturumData.xlsx")
        ids = neworenciToturum1["okulno"]
        new = neworenciToturum1[ids.isin(ids[ids.duplicated()])].sort_values("okulno")
        new = new[['okulno','adisoyadi',	'duzey',	'ders',	'tarih',	'saat','yer'	,'sinifalan']]
        df = df.append(new)
        #new.to_excel(path+tarih+saat+"_Oturum.xlsx", index=False)

df.to_excel(path+"Eylul_Oturum.xlsx", index=False)