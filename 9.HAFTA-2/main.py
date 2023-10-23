# def Kilolar():
#     dosya=open("sinif.txt","r",encoding="utf-8")
#     ogrenciler=dosya.readlines()
#     kilolar=[]
#     isimler=[]
#     for i in ogrenciler:
#         kilolar.append(float(i.split(" ")[0]))
#         isimler.append(i.split(" ")[1])
#     print(kilolar)
#     print(isimler)
#     print(sum(kilolar)/len(kilolar))
#     print(isimler[kilolar.index(max(kilolar))])
#     print(isimler[kilolar.index(min(kilolar))])
#
# Kilolar()
##DATETIME##
# import datetime #1.yöntem projeye dahil etmek için.
import datetime
from datetime import * # * ifadesi datetime içerisindeki herşeyi dahil et anlamına gelir

# suan=datetime.now() #
# bugun=datetime.today() #

# print(bugun.date()) #Date ifadesi ay gün yıl sonucunu verir.
# print(bugun.time()) #Time saat saniye salise sonucunu verir.
# print(bugun.year) #Geri yılı int olarak döndürür.
# print(bugun.month) #Ay bilgisini int olarak verir.
# print(bugun.day) #Gun bilgisini int olarak verir.
# print(bugun.hour) #Saat bilgisini int olarak verir.
# print(bugun.minute) #Dakika bilgisini int olarak verir.
# print(bugun.second) #Saniye bilgisini int olarak verir.

#El ile tarih verme #Verilen tarih bir küme olarak algılanır.
# tarih=(2021,11,23)
# print(type(tarih))
# print(tarih)

zaman=datetime.now()

# print(datetime)

# print(zaman.strftime("%d/%m/%y"))
# print(zaman.strftime("%d/%m/%Y"))
# print(zaman.strftime("%d.%m.%Y %H:%M:%S"))

"""
%d -> Sayısal Gün
%m -> Sayısal Ay
%Y -> Sayısal olarak Yılı 4 haneli
%y -> Sayısal olarak Yılı 2 haneli verir
%H -> Sayısal olarak Saati verir
%M -> Sayısal olarak Dakikayı verir
%S -> Saniye verir
%A -> Sözel olarak gün adını verir
%a -> Sözel olarak gün adını 3 karakter
%D -> AY/GUN/YIL
%b -> yazı ile 3 karakter ay adı
%B -> Yazı ile ayı tamamen yazdırır


"""
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")
#
# print(zaman.strftime("%A"))
# print(zaman.strftime("%a"))
# print(zaman.strftime("%b"))
#SORU GUN-AY-YIL Saat:Dakika:Saniye--Günadı konsola yazdırın.

# x=datetime.now()
# print(x.strftime("%d-%m-%Y %H:%M:%S--%A--%B"))

#Bir Şirket Otomasyonu Tasarlayınız.
#İnsan Kaynakları,Muhasebe, Ve Bilgi işlem birimleri olsun
#Her personel kendi birim adıyla oluşturulan txt dosyasına,
#İsim,Soyisim,Doğumyılı başlıkları olacak
#Personel ekleme,güncelleme,Silme ve Birime göre listeleme işlemlerini yapacak
#Bir menü tasarlayın ve işlemler bu menü üzerinden ilerlesin.