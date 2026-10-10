# Soru 8: İki basamaklı bir sayının rakamları toplamını bulan program

sayi = int(input("İki basamaklı bir sayı giriniz: "))

if sayi < 10 or sayi > 99:
    print("Hatalı işlem!")
else:
    onlar = sayi // 10
    birler = sayi % 10
    print("Rakamları toplamı:", onlar + birler)
