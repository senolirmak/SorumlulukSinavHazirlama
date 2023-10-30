#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:03:02 2023

@author: senol
"""

import pandas as pd
#import numpy as np


ogrenciler = "/home/senol/Pyprojeler/Sinav/sorumluluk/aktifOgrenciler_03012023.xlsx"
toplamDev ="/home/senol/Pyprojeler/Sinav/sorumluluk/ToplamDevamsızlık.xlsx"

ogrenci = pd.read_excel(ogrenciler)
devamsiz = pd.read_excel(toplamDev)

okulnosu = devamsiz.okulno.values

data=[]
si =""
for no in okulnosu:
    dic = {}
    newdf = ogrenci.query("okulno ==" +str(no))
    newdev = devamsiz.query("okulno ==" +str(no))
    if len(newdf['sinif'].values.flatten().tolist()) ==0:
        continue
    dic['sinif'] = newdf['sinif'].values.flatten().tolist()[0]
    dic['devam'] = newdev['toplam'].values.flatten().tolist()[0]
    dd = dic.copy()
    data.append(dd)
    dic.clear()

ff = pd.DataFrame(data)

sinif = 9

s1 = ff.query("sinif == " +str(sinif)+" and  devam >= 5 and devam <= 10 ")
s2 = ff.query("sinif == " +str(sinif)+" and  devam >= 11 and devam <= 15 ")
s3 = ff.query("sinif == " +str(sinif)+" and  devam >= 16 and devam <=20 ")
s4 = ff.query("sinif == " +str(sinif)+" and  devam >= 21 and devam < 70")
print("{}  {}  {}  {}".format(s1.shape[0],s2.shape[0],s3.shape[0],s4.shape[0]))
