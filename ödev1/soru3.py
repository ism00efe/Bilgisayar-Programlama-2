# Soru 3: Girilen kenar uzunluğuna göre yıldızlardan içi dolu kare çizen program

# Kullanıcıdan karenin kenar uzunluğu alınır
kenar = int(input("Karenin kenar uzunluğunu giriniz: "))

# Dış döngü satırları oluşturur (kenar kadar satır)
for satir in range(kenar):
    # İç döngü her satıra kenar kadar yıldız yazar
    for sutun in range(kenar):
        print("*", end=" ")
    # Bir satır bitince alt satıra geçilir
    print()
