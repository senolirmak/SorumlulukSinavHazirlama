#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:33:17 2023

@author: senolirmak
"""
from src.sinavGorevleri import gorevlerVeriOlustur, gorevleriYaz

tarih ="15/09/2023"
resmisayi = "0"
sheet_veri="Veriler"
sheet_ogretmen="Ogretmenler"
veriler_ods = "sinavHazirlama/data/2023/eylul/program/Eylül_2023_Sorumluluk_07Eylul.ods"
path = "sinavHazirlama/gorevler/2023/denek/"

data = gorevlerVeriOlustur(veriler_ods, sheet_veri, sheet_ogretmen)
gorevleriYaz(data, path, tarih, resmisayi)