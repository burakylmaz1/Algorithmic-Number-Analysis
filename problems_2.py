sayı=input("sayı giriniz")
basamak_sayısı=len(sayı)
sayı=int(sayı)
toplam=0
basamak=0
gecici_sayı=sayı
while(sayı>0):
    basamak=sayı%10
    toplam+=basamak**basamak_sayısı
    sayı=sayı//10
if(toplam==gecici_sayı):
    print(gecici_sayı,"armstrong sayısıdır.")
else:
    print(gecici_sayı,"armstrong sayısı değildir")








