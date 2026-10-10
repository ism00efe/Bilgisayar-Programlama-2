# Soru 6: Kullanıcı 0 girene kadar girilen sayıların toplamını hesaplayan program

# Toplam başlangıçta 0'dır
toplam = 0

# Döngüye girmeden önce ilk sayı alınır
sayi = int(input("Bir sayı giriniz (çıkmak için 0): "))

# Kullanıcı 0 girmediği sürece döngü devam eder
while sayi != 0:
    # Girilen sayı toplama eklenir
    toplam += sayi
    # Yeni sayı istenir
    sayi = int(input("Bir sayı giriniz (çıkmak için 0): "))

# 0 girildiğinde döngü biter ve toplam yazdırılır
print("Girilen sayıların toplamı:", toplam)
