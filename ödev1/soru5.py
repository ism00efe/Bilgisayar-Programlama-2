# Soru 5: 100 ile 999 arasındaki, N sayısına tam bölünebilen sayıları yazdıran program
# (Soruda istendiği için döngü olarak while kullanılmıştır)

# Kullanıcıdan bölen sayı (N) alınır
n = int(input("N sayısını giriniz: "))

# Bir sayı 0'a bölünemeyeceği için önce bu durum kontrol edilir
if n == 0:
    print("Bir sayı 0'a bölünemez.")
else:
    # Kontrole aralığın başlangıcı olan 100'den başlanır
    sayi = 100

    # 999'a kadar (999 dahil) her sayı tek tek kontrol edilir
    while sayi <= 999:
        # Bölümden kalan 0 ise sayı N'e tam bölünüyordur
        if sayi % n == 0:
            print(sayi)
        # Bir sonraki sayıya geçilir (bu satır olmazsa döngü sonsuza kadar sürer)
        sayi += 1
