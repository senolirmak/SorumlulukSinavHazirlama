#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:32:25 2023

@author: senol
"""

import pandas as pd
from pandas_ods_reader import read_ods

from fpdf import FPDF

# gereksiz uyarıları kapatalım
import warnings
warnings.filterwarnings('ignore')


def simple_table(data, path, filename, tarih="04/09/2023", resmisayi="8108396", spacing=2.1):
    data = data
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_font('LiberationSerif-Regular','','/usr/share/fonts/liberation-serif/LiberationSerif-Regular.ttf',uni=True)
    pdf.add_font('LiberationSerif-Bold','','/usr/share/fonts/liberation-serif/LiberationSerif-Bold.ttf',uni=True)
    pdf.add_page()
    
    pdf.set_font("LiberationSerif-Regular", size=12)
    line_height = pdf.font_size
    pdf.ln(line_height)
    #pdf.image("logo.png", x=20, y=10, w=10)
    pdf.set_x(50)
    pdf.multi_cell(100,line_height, txt="T.C.", align="C")
    pdf.set_x(50)
    pdf.multi_cell(100, line_height, txt="ALTINDAĞ KAYMAKAMLIĞI", align="C")
    pdf.set_x(50)
    pdf.multi_cell(100, line_height, txt="Altındağ Mesleki ve Teknik Anadolu Lisesi", align="C")
    pdf.set_x(50)
    pdf.multi_cell(100, line_height, txt="Müdürlüğü", align="C")
    pdf.ln(line_height)
    pdf.set_xy(20,46)
    pdf.multi_cell(100, 4, txt="Sayı  : 26904346-125.01-"+resmisayi, align="L")
    pdf.set_xy(170,46)
    pdf.multi_cell(50, 4, txt=tarih, align="L")
    pdf.set_xy(20,51)
    pdf.multi_cell(190, 4, txt="Konu : Sınav Görevi", align="L")
    pdf.ln(line_height*4)
    pdf.multi_cell(0, 4, txt="Sayın, "+filename , align="C")
    #pdf.set_font("LiberationSerif-Bold", size=12)

    text = ["Okulumuzda 18-22 Eylül 2023 tarihleri arasında yapılacak Eylül dönemi SORUMLULUK",
            "sınavlarında görevlendirildiniz. Sınav görevinizle ilgili bilgiler aşağıda belirtilmiştir. Sınav/sınavları",
            "sağlıklı bir şekilde M.E.B. Ortaöğretim Kurumları Yönetmeliğinin ilgili maddelerine göre (madde",
            "45, 47, 48, 49 ve 58) yürütmeniz ve sınavla ilgili evrakları sınav dönemi bitiminde okul",
            "müdürlüğüne teslim etmeniz gerekmektedir."
            ]
        
    geregi = "Bilgilerinizi ve gereğini rica ederim."
    aciklama = [
                "1) Sınav Evrak Zarfı",
                "2) Sorumluluk Sınavı Soru/Cevap Kağıdı Zarfı",
                "3) Sorumluluk Sınavı Öğrenci Cevap Kağıdı",
                "4) Sorumluluk Sınavı Tutanağı",
                "5) Sorumluluk Sınavı Sarf Tutanağı",
                "6) Sorumluluk Sınavı Not Çizelgesi",
                "*Sorumluluk Not Çizelgesi Doldurulup imzalandıktan sonra 1 nüsha fotokopisi zarfın içine konup, aslı müdür yardımcısına teslim edilecek."]
    
    """
    dipnot = ["Not;","Sınava girecek öğrenci sayısı 30 ve üzerinde ise sınavda görevlendirilen diğer",
        "öğretmen bulunmakta olup sınav saatinden 2 saat önce sınav sorularını hazırlamak",
        "için bir araya gelmeniz gerekmektedir."]
    """    

    yy = pdf.get_y()+5
    for st, satir in enumerate(text):
        pdf.set_xy(20,yy+st*5)
        if st == 0:
            pdf.set_xy(35,yy+st*5)
        pdf.multi_cell(180, 4, txt=satir , align="L")
    
    yy = pdf.get_y()+5
    pdf.set_xy(35,yy)
    pdf.multi_cell(0, 4, txt=geregi , align="L") 
    pdf.ln(line_height)
    yy = pdf.get_y()
    pdf.set_xy(160,yy)
    pdf.multi_cell(30, 4, txt=tarih+"\n\nHasan BAYAR\nOkul Müdürü", align="C")   
    pdf.set_font("LiberationSerif-Bold", size=12)
    
    pdf.ln(line_height)
    
    header = ['Sınav Tarihi','Saati','Sınıf','Sınav Yapılacak Ders','Salon']
    yy = pdf.get_y()
    pdf.set_xy(20,yy+5)
    pdf.multi_cell(180, 4, txt="Sınav Tarihleri;" , align="L")
    pdf.set_font("LiberationSerif-Bold", size=10)
    pdf.ln(line_height)
    pdf.set_x(20)
    for count, datum in enumerate(header):
        
        if count in [1,2]:
            pdf.cell(15, line_height, datum, border=1, ln=0, align='C')
        elif count == 3:
            pdf.cell(100, line_height, datum, border=1, ln=0)
        else:
            pdf.cell(22, line_height, datum, border=1, ln=0,align='C')
    pdf.ln(line_height)
    
    pdf.set_font("LiberationSerif-Regular", size=9)
    line_height = pdf.font_size * 2.4

    for row in data:
        pdf.set_x(20)
        for count, datum in enumerate(row):
            if count in [1,2]:
                pdf.cell(15, line_height, datum, border=1, ln=0,align='C')
            elif count == 3:
                pdf.cell(100, line_height, datum, border=1, ln=0)
            else:
                pdf.cell(22, line_height, datum, border=1, ln=0,align='C')
        pdf.ln(line_height)
    
    pdf.ln(line_height)
    yy = pdf.get_y()
    pdf.set_xy(20,yy+5)
    pdf.set_font("LiberationSerif-Bold", size=11) 
    pdf.cell(0,10,txt="Teslim Edilecek Ekraklar;",align='L')
    pdf.ln(line_height)
    pdf.set_font("LiberationSerif-Regular", size=11)    
    for st, satir in enumerate(aciklama):
        pdf.set_x(20)
        pdf.multi_cell(180, 4, txt=satir , align="L")
    
    """
    pdf.ln(line_height*0.4)
    pdf.set_y(262)
    pdf.set_font("LiberationSerif-Regular", size=8)  
    for st, satir in enumerate(dipnot):
        pdf.set_x(20)
        pdf.multi_cell(0, 3, txt=satir , align="L")
    """
    
    pdf.output(path+filename+'_table.pdf')

def haftaGunler(w:int=0):
    gun=['Pazar','Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi']
    return gun[w]


def gorevlerVeriOlustur(veriler_ods, sheet_veri, sheet_ogretmen):

    gorevli = read_ods(veriler_ods,sheet_veri)
    kisiler = read_ods(veriler_ods,sheet_ogretmen)

    codes, ogretmenler = pd.factorize(kisiler['gorevli'])


    data = []
    for u in ogretmenler:
        kisi = u
        new1 = gorevli.query("gorevli1 == '"+kisi+"' or gorevli2 == '"+ kisi+"'")
        new2 = new1[['gorevli1','tarih','saat','duzey','ders','yer']]
        #new2['gorevli']= (u)
        new2.gorevli1[new2.gorevli1 != u] = u
        for g in new2.iterrows():
            data.append(g[1])
    
    df_data = pd.DataFrame(data)
    df_data['tarih'] = pd.to_datetime(df_data['tarih'], errors='coerce').dt.strftime("%d.%m.%Y")
    #df_data['saat']= df_data['saat'].astype(str)
    df_data['saat']=[x[-8:][:5] for x in df_data['saat'].astype(str)]
    return df_data

def gorevleriYaz(df_data, path, tarih, resmisayi):

    codes, ogretmenler = pd.factorize(df_data['gorevli1'])
    ogretmenler = ogretmenler.tolist()
    
    for u in ogretmenler:
        datakisi = df_data.query("gorevli1 == '"+u+"'")
        newdatakisi = datakisi[['tarih','saat','duzey','ders','yer']]
        a=list(newdatakisi.itertuples(index=False, name=None))
        simple_table(a,path, u,tarih, resmisayi)



