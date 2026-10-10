# Soru 1: İki basamaklı iki farklı sayının ortak rakamlarını bulan program

sayi1 = int(input("Birinci iki basamaklı sayıyı giriniz: "))
sayi2 = int(input("İkinci iki basamaklı sayıyı giriniz: "))

if sayi1 < 10 or sayi1 > 99 or sayi2 < 10 or sayi2 > 99:
    print("Lütfen iki basamaklı sayılar giriniz.")
elif sayi1 == sayi2:
    print("Lütfen iki farklı sayı giriniz.")
else:
    # Basamakları ayrı ayrı belirleme
    onlar1 = sayi1 // 10
    birler1 = sayi1 % 10
    onlar2 = sayi2 // 10
    birler2 = sayi2 % 10

    print(sayi1, "-> onlar basamağı:", onlar1, ", birler basamağı:", birler1)
    print(sayi2, "-> onlar basamağı:", onlar2, ", birler basamağı:", birler2)

    # Ortak rakamları bulma (aynı rakam iki kez yazılmasın)
    ortak = []
    for rakam in [onlar1, birler1]:
        if (rakam == onlar2 or rakam == birler2) and rakam not in ortak:
            ortak.append(rakam)

    if len(ortak) > 0:
        print("Ortak rakamlar:", *ortak)
    else:
        print("Ortak rakam yoktur.")
