# Soru 4: Girilen sayıların aritmetik ortalamasını hesaplayan program

adet = int(input("Kaç adet sayı gireceksiniz? "))

if adet <= 0:
    print("Sayı adedi 0'dan büyük olmalıdır.")
else:
    toplam = 0
    for i in range(adet):
        sayi = float(input(str(i + 1) + ". sayıyı giriniz: "))
        toplam += sayi

    ortalama = toplam / adet
    print("Aritmetik ortalama:", ortalama)
