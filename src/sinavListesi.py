#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 01:44:30 2023

@author: senolirmak
"""

import pandas as pd
import numpy as np

class cozumDuzenleXLSX:
    def __init__(self, dataDersVeri_xls, dataDersKodu_xls):
        self.df_data = pd.read_excel(dataDersVeri_xls)
        self.df_kodd = pd.read_excel(dataDersKodu_xls)

    def getDersAdi(self, derscode):
        newdf = self.df_kodd.query("derskodu == '"+derscode+"'")
        if newdf.ders.values.size > 0:
            return newdf.ders.values[0]
        return None
    
    def getDersCodu(self, dersadi):
        newdf = self.df_kodd.query("ders == '"+dersadi+"'")
        if newdf.derskodu.values.size > 0:
            return newdf.derskodu.values[0]
        return None
    
    @staticmethod
    def unique(list1):
        x = np.array(list1)
        return np.unique(x).tolist()

    def sinavdakiOgrenciler(self, derskodu):
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

