#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:04:18 2023

@author: senolirmak
"""

from src.sinavCozum import SinavProgramiUret
import multiprocessing

def worker_function(xcz, secim, cakisma, uzunluk, result_queue):
    paket = []
    parm =[secim,uzunluk,cakisma]
    try:
        cz1 = program.cozumOrnekleme(xcz, secim, cakisma, uzunluk)
        paket.append(cz1)
        paket.append(parm)
        if isinstance(cz1, list) and len(cz1) > 0:
            result_queue.put(paket)
    except Exception as e:
        result_queue.put(e)

def sinavListeCalis(cozumluler:list, parametre:dict):
    #cakisma = cakisma
    #uzunluk = cozumuzunluk
    result_queue = multiprocessing.Queue()
    coreCount = multiprocessing.cpu_count()
    
    processes = []
    
    for i in range(0,coreCount):
        secim = parametre['secim'] # type: ignore
        uzunluk = parametre['uzunluk'] # type: ignore
        cakisma = parametre['cakisma'][i] # type: ignore
        process = multiprocessing.Process(target=worker_function, args=(cozumluler, secim, cakisma, uzunluk, result_queue))
        process.start()
        processes.append(process)
    

    for process in processes:
        process.join()

    cz2 = []
    while not result_queue.empty():
        result = result_queue.get()
        cz2.append(result)
        
        print("Çözüm paremetreleri secim:{},uzunluk:{},cakisma:{}".format(result[1][0],result[1][1],result[1][2].values()))
        print("Üretilen {}. çözüm, {} grubtan oluşmakta".format(len(cz2),len(result[0])))
        
        for sayi, cozum in enumerate(result[0]):
            print(cozum, end=',')
            print("\r")
            
        print(cozumCakismaGoster(result[0]))
        
        """
        if isinstance(result, list):
            if len(result) > 0:
                cz2.append(result)
                print("Üretilen {}. çözüm, {} elemanlı {} grubtan oluşmakta".format(len(cz2),len(result[0]),len(result)))
                for sayi, cozum in enumerate(result):
                    print(cozum, end=',')
                    print("\r")
                    
            print(cozumCakismaGoster(result))
        """
    # Rest of your code

def cozumCakismaGoster(cozumOrnek:list):

    cozumcakisma= 0
    dk = []
    for count, xcozum in enumerate(cozumOrnek):
        cozumcakisma= program.cozumOrnekKontrol(xcozum)[0]
        dk.append("Çkş:{}".format(cozumcakisma))
        #print("\r")
    
    return dk

def kalanDersListesi(xcozum):
    derslerKalan = list(set(program.sorumluDersler)-set(program.kismiCozumler_toList(xcozum)))

    print("+++++++++++++++++++++++++")
    print("Kalan ders saysı {}".format(len(derslerKalan)))
    print(derslerKalan)

    for u in derslerKalan:
        print("['{}']".format(u), end=",\n")
    
if __name__ == "__main__":
    
    dataDers = "./data/2023/eylul/islenmis/2023_DersCikti_Eylül.xlsx"
    dersKodu ="./data/2023/eylul/islenmis/2023_Kod_Eylül.xlsx"

    program = SinavProgramiUret(dataDers, dersKodu)
    sinavsayisi = program.sinavSayisi
    
    xcozum = [
        ['ders_1909', 'ders_9110', 'ders_7912', 'ders_1210', 'ders_5712', 'ders_0009', 'ders_4312', 'ders_1109'],
        ['ders_7812', 'ders_3512', 'ders_4211', 'ders_7711', 'ders_0510', 'ders_3210', 'ders_0309', 'ders_0810'],
        ['ders_4111', 'ders_7010', 'ders_8411', 'ders_0710', 'ders_8811', 'ders_4709', 'ders_6409', 'ders_2010'],
        ['ders_2012', 'ders_2211', 'ders_1409', 'ders_2110', 'ders_2911', 'ders_0310', 'ders_3911', 'ders_7411'],
        ['ders_0010', 'ders_9010', 'ders_8111', 'ders_2510', 'ders_1809', 'ders_2410', 'ders_6810', 'ders_5011'],
        ['ders_2210', 'ders_0909', 'ders_0409', 'ders_5111', 'ders_1412', 'ders_9411', 'ders_2310'],
        ['ders_5912', 'ders_2009', 'ders_7311', 'ders_2711', 'ders_5311', 'ders_8911', 'ders_4412'],
        ['ders_0509', 'ders_5211', 'ders_7211', 'ders_2811', 'ders_4910', 'ders_9311', 'ders_0112'],
        ['ders_0512', 'ders_1609', 'ders_6711', 'ders_3811', 'ders_5812', 'ders_8612', 'ders_7510'],
        ['ders_7112', 'ders_4011', 'ders_1511', 'ders_8211', 'ders_7611', 'ders_1009'],
        ['ders_9211', 'ders_5411', 'ders_1710', 'ders_2612', 'ders_0609', 'ders_3312'],
        ['ders_3711', 'ders_4611', 'ders_6011', 'ders_0809', 'ders_8711', 'ders_0110'],
        ['ders_8311', 'ders_1309', 'ders_2209', 'ders_8011', 'ders_1410', 'ders_5611'],
        ['ders_2511', 'ders_3611', 'ders_0709', 'ders_0209', 'ders_6910', 'ders_5510'],
        ['ders_6211', 'ders_3011', 'ders_6511', 'ders_8511', 'ders_4511'],
        ['ders_6611'],
        ['ders_3412'],
        ['ders_1509'],
        ['ders_4809'],
        ['ders_6111'],
        ]
    
    kalanDersListesi(xcozum)
    parametres = {
        'secim':4,
        'uzunluk':6,
        'cakisma':[{'_alt':0,'_ust':21},
                   {'_alt':0,'_ust':13},
                   {'_alt':1,'_ust':5},
                   {'_alt':2,'_ust':6},
                   {'_alt':3,'_ust':7},
                   {'_alt':4,'_ust':8},
                   {'_alt':5,'_ust':9},
                   {'_alt':6,'_ust':10},
                   ]
        }


    sinavListeCalis(cozumluler=xcozum, parametre=parametres)
