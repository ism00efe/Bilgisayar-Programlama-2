# Soru 6: Kullanıcı 0 girene kadar girilen sayıların toplamını hesaplayan program

toplam = 0
sayi = int(input("Bir sayı giriniz (çıkmak için 0): "))

while sayi != 0:
    toplam += sayi
    sayi = int(input("Bir sayı giriniz (çıkmak için 0): "))

print("Girilen sayıların toplamı:", toplam)
