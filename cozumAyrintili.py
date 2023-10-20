#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:54:24 2023

@author: senolirmak
"""

import pandas as pd
import numpy as np
import random
from collections import Counter

dataDers = "./liste/2023_DersCikti_Eylul.xlsx"
dersKodu ="./liste/2023_Kod_Eylul.xlsx"

df_data = pd.read_excel(dataDers)
df_kodd = pd.read_excel(dersKodu)
sorumluDersler = df_kodd.derskodu.values

for ders in sorumluDersler:
    df_data[ders]=df_data[ders].fillna(0)
    df_data[ders]=df_data[ders].astype(int)


def degistirAlan(_list1):
    _list = [['TEKNOLOJİLERİ',''],
             ['MAKİNE VE TASARIM','TASARIM'],
             ['TEKNOLOJİSİ',''],
             ['MOBİLYA VE İÇ MEKÂN TASARIMI','MOBİLYA'],
             ['ELEKTRİK ELEKTRONİK','ELEKTRİK']]

    sub = dict(_list)
    for key, val in sub.items():
        for idx, ele in enumerate(_list1):
            if key in ele:
                _list1[idx] = ele.replace(key, val).strip() 
    return _list1

def sinavAlan(derskodu):
    
    newdf = df_kodd.query("derskodu == '"+derskodu+"'")
    alan = newdf.alan.values
    return alan


def sinavdakiAlanlar(xcozum, alansinir=2):
    f = list()
    for veri in xcozum:
        v = degistirAlan(sinavAlan(veri))
        f.append(v[0])
  
    branslar = Counter(f)
    
    m = max(branslar.values())
    if m > alansinir:
        if 'ELEKTRİK' in branslar.keys():
            if branslar['ELEKTRİK'] < 4 and  branslar['ELEKTRİK'] == m:
                return False
        return True
    
    return False

    
def sinavdakiOgrenciler(derskodu):
    _ders = derskodu
    newdf = df_data.query(_ders+" == 1")
    ogrenciNo = newdf.okulno.values
    if ogrenciNo.size > 0:
        return set(ogrenciNo.tolist())
    return None

def cozumlist_toSet(cozum):
    setCozumler = set()

    for u in cozum:
        for v in u:
            setCozumler.add(v)
    return setCozumler

def cakismaBayrak(_cozumlist, scakisma = 3):
    
    ogrenciler = []
    h=0
    maxz = 0
    
    if sinavdakiAlanlar(_cozumlist):
        return h, True
    
    for ders in _cozumlist:
        for ogno in sinavdakiOgrenciler(ders):
            ogrenciler.append(ogno)
    
    c = Counter(ogrenciler)
    maxz = max(c.values())
    
    if maxz > 2 :
        return h, True
    
    if maxz <= 2 :
        for u in c.values():
            if u==2:
                h+= 1
                
        if h <= scakisma:
            return h, False

    return h, True

def cozumOrnekleme(cozum = list(), kalan=list(),secim =9, cakisma = 3):
    A = set(cozum)
    B = set(kalan)
    dersler = A.union(B)
    dersler = list(dersler)
    random.shuffle(dersler)
    print("Çözülecek ders sayısı:{}".format(len(dersler)))
    
    
    tempcozum = []
    sinavcakisma = 0
    tempcakisma = cakisma
    dkontrol = True
    kontrol = True
    sayac = 0
    
    while dkontrol:
        sayac += 1
        ornek = np.random.choice(dersler,secim,replace=False)
        ornekcozum = ornek.tolist()
        sinavcakisma,  kontrol = cakismaBayrak(ornekcozum, scakisma=cakisma)

        if not kontrol :
            if sinavcakisma <= tempcakisma:#and len(ornekcozum) == secim:
                tempcakisma = sinavcakisma
                cozum = ornekcozum
                continue
            """
            if sinavcakisma == tempcakisma: #and len(cozumlist) == secim:
                tempcakisma = tempcakisma
                tempcozum = tempcozum
                #dkontrol = False
            """
            
        if sayac == 1000:
            dkontrol = False
                
    
    if len(tempcozum) == 0:
        return tempcozum, dersler , cakisma
    
    if len(tempcozum) == secim : 
        #print("Sınavı çakışan öğrenci sayısı: {}".format(cakisma))
        #print(tempcozum)
        a = set(cozum)-set(tempcozum)
        b = set(tempcozum)-set(cozum)
        kalan = a.union(set(kalan))
        kalan = kalan-b
        kalan = list(kalan)
        #print("Çözümden sonra kalan {} ".format(len(kalan)))      
        return tempcozum, kalan, tempcakisma


_cozum =[
    ['ders_1510', 'ders_1810', 'ders_2312', 'ders_0410', 'ders_7211', 'ders_3212', 'ders_1109'],
    ['ders_3911', 'ders_8812', 'ders_1009', 'ders_6710', 'ders_4711', 'ders_6911', 'ders_7711'],
    ['ders_3112', 'ders_8011', 'ders_1712', 'ders_6311', 'ders_0709', 'ders_8310', 'ders_5811'],
    ['ders_7611', 'ders_0309', 'ders_6211', 'ders_2511', 'ders_0409', 'ders_2210', 'ders_1310'], 
    ['ders_8211', 'ders_3312', 'ders_8511', 'ders_4111', 'ders_0310', 'ders_5711', 'ders_0110'],
    ['ders_3811', 'ders_5211', 'ders_0010', 'ders_5911', 'ders_1609', 'ders_5411', 'ders_7110'], 
    ['ders_1711', 'ders_1911', 'ders_6811', 'ders_4911', 'ders_0509', 'ders_2611', 'ders_1909'],
    ['ders_7511', 'ders_1910', 'ders_1509', 'ders_7311', 'ders_8410', 'ders_7411', 'ders_3511'],
    ['ders_3011', 'ders_7911', 'ders_4211', 'ders_7011', 'ders_1410', 'ders_8912', 'ders_0112'],
    ['ders_6109', 'ders_0009', 'ders_8111', 'ders_4811', 'ders_9011', 'ders_2911', 'ders_2711'],
    ['ders_2110', 'ders_0609', 'ders_5612', 'ders_0710', 'ders_3412', 'ders_0111', 'ders_5111'],
    ['ders_8709', 'ders_2811', 'ders_5310', 'ders_5512', 'ders_6411', 'ders_1112', 'ders_2010'],
    ['ders_2211', 'ders_0209', 'ders_5011', 'ders_0910', 'ders_6510', 'ders_2411', 'ders_3611'],
    ['ders_7811', 'ders_8611', 'ders_4010', 'ders_4409', 'ders_6011', 'ders_6610', 'ders_4610'],
    ]

_cozum0 = []

for u in _cozum:
    for v in u:
        _cozum0.append(v)

#print((set(sorumluDersler)))

_kalan = list(set(sorumluDersler)-set(_cozum0))
print("Kalan ders sayısı {}".format(len(_kalan)))
cakisma = 30



for count, u in enumerate(_cozum):
    
    secim = len(u) + 1
    print("{}. Grup Çözülüyor ...".format(count+1))
    random.shuffle(_kalan)
        
    if len(_kalan) == 0:
        print("Eklenecek ders bitti")
        break
        
    cz2, _kalan0, _cakisma = cozumOrnekleme(cozum=u, kalan=_kalan, secim=secim, cakisma=cakisma)
    if len(cz2) == 0:
        print("Yeni çözüm yok")
        continue
        
    if len(cz2) > 0 :
        _cozum[count] = cz2
        _kalan = _kalan0
        print("---- Çözüm ----")
        print("Sınavı çakışan öğrenci sayısı: {}".format(_cakisma))
        print(cz2)
        print("---- ---- ----")
        print("Kalan Ders Sayı {}\n".format(len(_kalan)))    
        continue

for cz in _cozum:
    print(cz, end=',')
    print()
 
print("-----------------------")
print("Kalan Dersler........\n {} ".format(_kalan))
print("-----------------------")
#print(ekle_)

    
    