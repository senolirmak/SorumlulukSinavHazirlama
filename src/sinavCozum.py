#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:20:06 2023

@author: senolirmak
"""

import pandas as pd
import numpy as np
import random
from collections import Counter
from pandas_ods_reader import read_ods


class SinavProgramiUret:
    def __init__(self, dataDersVeri_xls, dataDersKodu_xls):
        self.df_data = pd.read_excel(dataDersVeri_xls)
        self.df_kodd = pd.read_excel(dataDersKodu_xls)
        self.sorumluDersler = set()
        self.sinavSayisi = 0
              
        
        if len(self.df_kodd.derskodu.values) > 0 :
            if self.derslerdeTekrarVar(self.df_kodd.derskodu.values):
                self.sorumluDersler = set(self.df_kodd.derskodu.values)
                self.sinavSayisi = len(self.sorumluDersler)
            else:
                print("Öğrencilerin sorumlu derslerinde tekrar var. Kontrol ediniz.")
                return None

    def sinavAlan(self, derskodu):
        if isinstance(derskodu, str):
            newdf = self.df_kodd.query("derskodu == '"+derskodu+ "'")
            alan = newdf.alan.values
        else:
            print(derskodu)
            print("Burada Hata oldu")
            return None
        
        return alan

    def sinavdakiOgrenciler(self, derskodu):
        _ders = derskodu
        newdf = self.df_data.query(_ders+" == 1")
        ogrenciNo = newdf.okulno.values
        if ogrenciNo.size > 0:
            return set(ogrenciNo.tolist())
        return None
    
    def sinavAlanKontrol(self, cozum:list(), sinir:int =2):
        f = list()
        v = []
        for veri in cozum:
            for x in self.sinavAlan(veri):
                v = x.split("-")
                
            if len(v)>1:
                for i in range(0, len(v)):
                    f.append(v[i])
            else:
                f.append(v[0])
                
        branslar = Counter(f)      
        m = max(branslar.values())
        
        if m in range(0, sinir):
            if 'MOBİLYA' in branslar.keys():
                if branslar['MOBİLYA'] > 1:
                    return True
            """
            if 'TASARIM' in branslar.keys():
                if branslar['TASARIM'] > 1:
                    return True
            """    
            if 'FELS' in branslar.keys():
                if branslar['FELS'] > 1:
                    return True
                
            if 'KIMY' in branslar.keys():
                if branslar['KIMY'] > 1:
                    return True
                
            if 'FIZK' in branslar.keys():
                if branslar['FIZK'] > 1:
                    return True
                
            if 'BIYO' in branslar.keys():
                if branslar['BIYO'] > 1:
                    return True
            
            if 'COGR' in branslar.keys():
                if branslar['COGR'] > 1:
                    return True
            
            if 'TARH' in branslar.keys():
                if branslar['TARH'] > 1:
                    return True
            
            if 'MATE' in branslar.keys():
                if branslar['MATE'] > 1:
                    return True
            
            if 'YABD' in branslar.keys():
                if branslar['YABD'] > 1:
                    return True
                
            if 'BEDE' in branslar.keys():
                if branslar['BEDE'] > 1:
                    return True
                
            if 'TDVE' in branslar.keys():
                if branslar['TDVE'] > 2:
                    return True
                
            return False
        
        return True
    
    def getDersAdi(self, derscode):
        newdf = self.df_kodd.query("derskodu == '"+derscode+"'")
        if newdf.ders.values.size > 0:
            return newdf.ders.values[0]
        return None
    
    def sinavTakvimiOgrenciler(self, verilerODS, verilerODS_sheet):
        sinavVerileri = read_ods(verilerODS,verilerODS_sheet)
        renameSutun = {'SINIF DÜZEYİ':'duzey','SINAV YAPILACAK DERS':'ders',
                       'TARİHİ':'tarih', 'SINAV SAATİ':'saat', 'SINAV YERİ':'yer'}
        sinavVerileri.rename(columns = renameSutun, inplace = True)
        sinavVerileri.dropna(inplace=True)
        
        dersmatris = self.df_data
        derskodlari = self.df_kodd
        sinavkodList = derskodlari['derskodu'].tolist()
        
        kodlar = derskodlari[['duzey', 'ders', 'derskodu']]
        kodlar['duzey'].astype(int)
        sinav = sinavVerileri[['duzey',	'ders', 'tarih', 'saat', 'yer']]
        sinav['saat']=[x[-8:][:5] for x in sinav['saat'].astype(str)]
        sinav['tarih'] = pd.to_datetime(sinav['tarih'], errors='coerce').dt.strftime("%d.%m.%Y")
        sinav['duzey'] = [int(x.split(".")[0]) for x in sinav['duzey']]
        sinav = pd.merge(sinav, kodlar, on=['duzey', 'ders'], how='left')
        data = []
        for ders in sinavkodList:
            veri = dict()
            for ogrenci in self.sinavdakiOgrenciler(ders):
                veri['okulno'] = ogrenci
                veri['derskodu'] = ders
                x = veri.copy()
                data.append(x)
                veri.clear()
                
        ogrenciSinavi = pd.DataFrame(data)
        
        sinavT = pd.merge(ogrenciSinavi, sinav, on=['derskodu'], how='left')
        ogrencibilgisi = dersmatris[['okulno', 'adisoyadi', 'okul', 'sinif', 'sube', 'alan']]
        ogrenciT = pd.merge(sinavT, ogrencibilgisi, on=['okulno'], how='left')
        ogrenciT['sinifalan'] = ogrenciT.apply(lambda x: x['okul'] +"-"+ str(x['sinif'])+"/"+ x['sube']+" Şubesi " +"("+ x['alan']+" ALANI)", axis=1)
        neworenciT = ogrenciT[['okulno', 'adisoyadi','derskodu','duzey','ders', 'tarih', 'saat', 'yer','sinifalan']]
        neworenciT['duzey'] = neworenciT.apply(lambda x : str(x.duzey).split(".")[0]+". SINIF", axis=1)
        neworenciT = neworenciT.dropna(axis=0)
        neworenciT = neworenciT.reset_index(drop=True)
        neworenciT.to_excel("SinavTakvimiOgrenciler.xlsx", index=False)
        #neworenciT = neworenciT.sort_values(by=['tarih','saat'], ascending=True)
        
        return neworenciT
    
    def sinavOturumDersAyrintili(self, derskodu):
        _ders = derskodu
        newdf = self.df_data.query(_ders+" == 1")
        newkod = self.df_kodd.query("derskodu =='"+_ders+"'")
        ogrenciNo = newdf.okulno.values
        alan = newkod.alan.values
        duzey = newkod.duzey.values
        
        if ogrenciNo.size > 0:
            dersOgrenci = {'Duzey':duzey[0],
                           'DersKodu':_ders,
                           'Ders':self.getDersAdi(_ders),
                           'Alan':alan[0],
                           'Okulno':ogrenciNo.tolist(),
                           'Sayı': len(ogrenciNo.tolist())}
            
            return dersOgrenci
        return None
    
    def ogrenciSinavCakismaListesi(self, cozum:list()):
        sinavListesi = []
        
        for ders in cozum:
            sinav = {}
            for ogno in self.sinavdakiOgrenciler(ders):
                sinav['ders'] = ders
                sinav['okulno'] = ogno
                xc = sinav.copy()
                sinavListesi.append(xc)
                sinav.clear()
            
            
                
        sinavListesiData = pd.DataFrame(sinavListesi)
        sinavLisDat = sinavListesiData['okulno'].duplicated()
        print(sinavLisDat.tolist())
        sinavListesiData['cakisma'] = sinavLisDat.tolist()
        # Sinavı cakışan öğrenci numaralrı seçildi
        #cakismalar = sinavListesiData['okulno'].duplicated()
        #sinavListesi['cakisma']=sinavLisDat
        
        sinavListesiData.to_excel("sinavCakismalari.xlsx", index=False)
        
    def sinavOgrenciKontrol(self, cozum:list(), cakisma:dict()={'_alt' : 0, '_ust' : 20},sinir:int = 2):
        ogrenciler = []
        h=0
        maxz = 0

        for ders in cozum:
            for ogno in self.sinavdakiOgrenciler(ders):
                ogrenciler.append(ogno)
        
        
        c = Counter(ogrenciler)
        maxz = max(c.values())
        #Burada Deiğişiklik yapıldı hiç çakışma istenmiyor
        if maxz > sinir :
            return h, True
        
        for u in c.values():
            if u==2:
                h+= 1
                    
        if h in range(cakisma['_alt'], cakisma['_ust']):
            return h, False
        
        return h, True

    def kismiCozumler_toList(self, kismiCozumler):
        listKismiCozumler = list()

        for u in kismiCozumler:
            for v in u:
                listKismiCozumler.append(v)
        return listKismiCozumler

    def derslerdeTekrarVar(self, dersler):
        c = Counter(dersler)
        maxz = max(c.values())
        if maxz > 1 :
            return False
        elif maxz == 1:
            return True
        else:
            return None
            
    def cozumOrnekKontrol(self, cozum:list(), cakisma:dict()={'_alt' : 0, '_ust' : 20}):
        
        cakismaSayisi = -1
        cakismaKontrol = False
        
        """
        if self.sinavAlanKontrol(cozum, 4):
            return cakismaSayisi , True
        """
        
        cakismaSayisi, cakismaKontrol = self.sinavOgrenciKontrol(cozum, cakisma)
        
        if cakismaKontrol or self.sinavAlanKontrol(cozum, 3):
            return cakismaSayisi , True
        
        return cakismaSayisi, False

    
    def cozumAyrintili(self, cozum = list(),  secim:int =7, kalan=list(), cakisma:int =2):
        dcakisma = dict()
        dcakisma['_alt'] = self.cozumOrnekKontrol(cozum)[0]
        dcakisma['_ust'] = dcakisma['_alt'] + 1 if dcakisma['_alt'] >=  cakisma else cakisma
      
        dersler = list(set(cozum).union(set(kalan)))
        random.shuffle(dersler)
        print("Çözülecek ders sayısı:{}".format(len(dersler)))
        
        
        tempcozum = []
        sinavcakisma = 0
        dkontrol = True
        kontrol = True
        sayac = 0
        
        while dkontrol:
            sayac += 1
            ornek = np.random.choice(dersler,secim,replace=False)
            ornekcozum = ornek.tolist()
            sinavcakisma,  kontrol = self.cozumOrnekKontrol(ornekcozum, dcakisma)

            if not kontrol :
                tempcozum = ornekcozum
                dkontrol = False
                
            if sayac == 1000:
                dkontrol = False
                    
        
        if len(tempcozum) == 0:
            dcakisma.clear()
            return tempcozum, dersler , sinavcakisma
        
        if len(tempcozum) == secim : 
            a = set(cozum)-set(tempcozum)
            b = set(tempcozum)-set(cozum)
            kalan = a.union(set(kalan))
            kalan = kalan-b
            kalan = list(kalan)
            dcakisma.clear()
            return tempcozum, kalan, sinavcakisma
    
    def cozumEkleAyrintili(self, cozum = list(), kalan=list(), secim:int =7, cakisma:int =2, eksecim:int = 3):
        dcakisma = dict()
        dcakisma['_alt'] = self.cozumOrnekKontrol(cozum)[0]
        dcakisma['_ust'] = dcakisma['_alt'] + 1 if dcakisma['_alt'] >=  cakisma else cakisma

        tempcozum = []
        sinavcakisma = 0
        dkontrol = True
        kontrol = True
        sayac = 0
        
        while dkontrol:
            sayac += 1
            ek_ = np.random.choice(kalan,eksecim,replace=False).tolist()
            #ek_ = ek_.tolist()
            dersler = list(set(cozum).union(set(ek_)))
            random.shuffle(dersler)
            sinavcakisma,  kontrol = self.cozumOrnekKontrol(dersler, dcakisma)
            
            if not kontrol :

                tempcozum = dersler
                dkontrol = False
                
            if sayac == 50:
                dkontrol = False
                    
        
        if len(tempcozum) == 0:
            dcakisma.clear()
            return tempcozum, cozum , sinavcakisma
        
        if len(tempcozum) >= secim : 
            #print("Sınavı çakışan öğrenci sayısı: {}".format(cakisma))
            #print(tempcozum)
            a = set(cozum)-set(tempcozum)
            b = set(tempcozum)-set(cozum)
            kalan = a.union(set(kalan))
            kalan = kalan-b
            kalan = list(kalan)
            #print("Çözümden sonra kalan {} ".format(len(kalan)))
            dcakisma.clear()
            return tempcozum, kalan, sinavcakisma
        
    def cozumOrnekleme(self, kismiCozumler=set(),secim:int =7, cakisma:dict()={'_alt' : 0, '_ust' : 20},uzunluk:int=15):
        
        derslerKalan = set(self.sorumluDersler)-set(self.kismiCozumler_toList(kismiCozumler))
        derslerList = list(derslerKalan)

        random.shuffle(derslerList)
        print("Çözülecek ders sayısı:{}\n".format(len(derslerList)))

        sinavcakisma = 0
        dkontrol = True
        kontrol = True
        dcozum = []
        sayac = 0
        
        while dkontrol:
            sayac += 1
            try:
                ornek = np.random.choice(derslerList,secim, replace = False)
                cozumlist = ornek.tolist()
                sinavcakisma,  kontrol = self.cozumOrnekKontrol(cozumlist, cakisma)
            except ValueError:
                print("Kalan ders sayısı, {} 'den az".format(secim))
                return None
            
            except KeyboardInterrupt:
                print("Program durdurulduğu için çözüm eksik veya oluşmadı")
                return dcozum
            
            if not kontrol :
                if len(set(self.kismiCozumler_toList(dcozum)).intersection(set(cozumlist))) == 0:
                    dcozum.append(cozumlist)
                    derslerKalan = set(derslerList)-set(cozumlist)
                    derslerList = list(derslerKalan)
            
            if sayac == 5000 and len(dcozum) < uzunluk:
                #print("Kalan ders sayısı:{}".format(len(derslerList)))
                dkontrol = False
                
            if len(dcozum) == uzunluk: # or len(derslerList) < secim:
                
                #print("Kalan ders sayısı:{}".format(len(derslerList)))
                dkontrol = False
        
        print("Kalan ders sayısı:{}".format(len(derslerList)))
        return dcozum

