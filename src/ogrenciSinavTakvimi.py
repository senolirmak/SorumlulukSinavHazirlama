#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:32:25 2023

@author: senol
"""

from fpdf import FPDF

# gereksiz uyarıları kapatalım
import warnings
warnings.filterwarnings('ignore')


def simple_table(datasinav:list(),dataogrenci:list(), path, filename, spacing=2.1):
    
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_font('LiberationSerif-Regular','','/usr/share/fonts/liberation-serif/LiberationSerif-Regular.ttf',uni=True)
    pdf.add_font('LiberationSerif-Bold','','/usr/share/fonts/liberation-serif/LiberationSerif-Bold.ttf',uni=True)
    pdf.add_page()
    
    pdf.set_font("LiberationSerif-Regular", size=10)
    line_height = pdf.font_size
    #pdf.set_xy(20,46)

    aciklama = [
                "Sınava Öncesi/Esnasında ,",
                "1) Sorumluluk Sınav Takvimi konrol ederek zamanında sınav solununda olunuz",
                "2) Sınav salonlarında herkes kendisine ait kalem, silgi, kalem ucu, kalemtraş vb alet",
                " ve aracı kullanacaktır. Başkasına ait alet ve araçların kullanılmasına izin",
                " verilmeyecektir. Bu sebeple tüm öğrencilerin sınavlara dersin özelliğine göre",
                " eksiksiz gelmesi esastır.",
                "3)Yönetici, öğretmen ve diğer okul personelinin uyarılarına bütün öğrenciler uymak",
                " zorundadır. kurallara aykırı ve sürekli olumsuz harekette bulunan öğrenciler gerekirse",
                " sınav salonundan ve okul binasından çıkartılacak, haklarında yasal işlem uygulanacaktır."]
    
    pdf.set_font("LiberationSerif-Bold", size=10)
    ogrencibaslik = ["Okul No","Adı ve Soyadı","Sınıf/Şube Alan"]
    l_height = pdf.font_size * 2.4
    pdf.set_x(20)
    for count, datum in enumerate(ogrencibaslik):
        if count ==0:
            pdf.cell(18, l_height, datum, border=0, ln=0, align='L')
        else:
            pdf.cell(60, l_height, datum, border=0, ln=0,align='L')
            
    pdf.ln(line_height)
    pdf.set_x(20)
    pdf.set_font("LiberationSerif-Regular", size=10)
    for row in dataogrenci:
        for count, datum in enumerate(row):
            if count ==0:
                pdf.cell(18, l_height, str(datum), border=0, ln=0, align='L')
            else:
                pdf.cell(60, l_height, datum, border=0, ln=0,align='L')
    
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

    for row in datasinav:
        pdf.set_x(20)
        for count, datum in enumerate(row):
            if count in [1,2]:
                pdf.cell(15, line_height, datum, border=1, ln=0,align='C')
            elif count == 3:
                pdf.cell(100, line_height, datum, border=1, ln=0)
            else:
                pdf.cell(22, line_height, datum, border=1, ln=0,align='C')
        pdf.ln(line_height)

    pdf.ln(pdf.font_size)
    pdf.set_font("LiberationSerif-Regular", size=10)    
    for st, satir in enumerate(aciklama):
        pdf.set_x(20)
        pdf.multi_cell(180, 4, txt=satir , align="L")
    
    
    pdf.output(path+filename+'_table.pdf')




