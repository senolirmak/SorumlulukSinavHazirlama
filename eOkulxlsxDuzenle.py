#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:39:07 2023

@author: senolirmak
"""
from src.veriduzenle_version01 import veriDuzenle

dosya_xls = "sinavHazirlama/data/2023/eylul/eokulveri/OOK12001R012_91.xlsx"

deveri = veriDuzenle(dosya_xls)
deveri.dataFrametoExcel("Eylül_02")