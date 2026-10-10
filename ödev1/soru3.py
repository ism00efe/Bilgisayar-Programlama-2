# Soru 3: Girilen kenar uzunluğuna göre yıldızlardan içi dolu kare çizen program

kenar = int(input("Karenin kenar uzunluğunu giriniz: "))

for satir in range(kenar):
    for sutun in range(kenar):
        print("*", end=" ")
    print()
