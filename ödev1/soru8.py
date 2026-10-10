# Soru 8: İki basamaklı bir sayının rakamları toplamını bulan program

# Kullanıcıdan sayı alınır
sayi = int(input("İki basamaklı bir sayı giriniz: "))

# Sayı 10'dan küçük veya 99'dan büyükse iki basamaklı değildir
if sayi < 10 or sayi > 99:
    print("Hatalı işlem!")
else:
    # Sayı onlar ve birler basamaklarına ayrılır
    onlar = sayi // 10
    birler = sayi % 10

    # İki rakam toplanarak sonuç yazdırılır
    print("Rakamları toplamı:", onlar + birler)
