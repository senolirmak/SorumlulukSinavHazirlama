#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:21:47 2023

@author: senol
"""
import pandas as pd
data_Kod ="./data/2023/eylul/islenmis/2023_Kod_Eylül.xlsx"
data_Brans ="./data/2023/eylul/islenmis/branslar.xlsx"

df_Kod = pd.read_excel(data_Kod)
df_Brans = pd.read_excel(data_Brans)
dfBrans =df_Brans[['ders','brans']]
sinav = pd.merge(df_Kod, dfBrans, on=['ders'], how='left')
sinav.replace(to_replace={'brans': 'alan'}, value=None, method=None)
derskodlarialanlar = sinav[['duzey',	'ders','derskodu','alan']]
derskodlarialanlar.to_excel("./data/2023/eylul/islenmis/2023_Kod_Eylül_Branlar_Eklenmis.xlsx", index=False)