import ftplib
import py7zr
import os
import datetime
from pathlib import Path

e = datetime.datetime.now()
dosyaAd="%s-%s-%s_%s-%s-%s" % (e.day, e.month, e.year,e.hour, e.minute, e.second)

with py7zr.SevenZipFile("C:\\Users\\pc\\Documents\\python_test\\" + dosyaAd+ ".7z", mode='w') as z: 
    z.writeall(r"C:\Users\pc\Documents\python_test\Hesaplar") #sıkıştırlacak klasör

YerelDosya = r"C:\\Users\\pc\\Documents\\python_test\\" + dosyaAd+ ".7z"
UzakDosya = "./Yedek/"+dosyaAd+ ".7z" #dosyanın hangi klasore ve hangi isimle yuklenecegi

session = ftplib.FTP('sunucu adresi', 'kullanici adi', 'sifre')
file = open(YerelDosya,'rb')                  
session.storbinary('STOR '+UzakDosya, file)    
file.close()                                    
session.quit()
os.remove(YerelDosya)
print("upload bitti...")





