# Soru 5: 100 ile 999 arasındaki, N sayısına tam bölünebilen sayıları yazdıran program
# (döngü olarak while kullanılmıştır)

n = int(input("N sayısını giriniz: "))

if n == 0:
    print("Bir sayı 0'a bölünemez.")
else:
    sayi = 100
    while sayi <= 999:
        if sayi % n == 0:
            print(sayi)
        sayi += 1
