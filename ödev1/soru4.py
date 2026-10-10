# Soru 4: Girilen sayıların aritmetik ortalamasını hesaplayan program

# Kullanıcıdan kaç sayı gireceği öğrenilir
adet = int(input("Kaç adet sayı gireceksiniz? "))

# Adet 0 veya negatifse ortalama hesaplanamaz (sıfıra bölme hatası olur)
if adet <= 0:
    print("Sayı adedi 0'dan büyük olmalıdır.")
else:
    # Girilen sayıların toplamı bu değişkende tutulur
    toplam = 0

    # Kullanıcıdan istenen adet kadar sayı alınır ve toplama eklenir
    for i in range(adet):
        sayi = float(input(str(i + 1) + ". sayıyı giriniz: "))
        toplam += sayi

    # Aritmetik ortalama = toplam / sayı adedi
    ortalama = toplam / adet
    print("Aritmetik ortalama:", ortalama)
