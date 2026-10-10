# Soru 1: İki basamaklı iki farklı sayının ortak rakamlarını bulan program

# Kullanıcıdan iki sayı alınır
sayi1 = int(input("Birinci iki basamaklı sayıyı giriniz: "))
sayi2 = int(input("İkinci iki basamaklı sayıyı giriniz: "))

# Sayıların iki basamaklı ve birbirinden farklı olup olmadığı kontrol edilir
if sayi1 < 10 or sayi1 > 99 or sayi2 < 10 or sayi2 > 99:
    print("Lütfen iki basamaklı sayılar giriniz.")
elif sayi1 == sayi2:
    print("Lütfen iki farklı sayı giriniz.")
else:
    # Onlar basamağı: sayının 10'a tam bölümü (// işlemi)
    # Birler basamağı: sayının 10'a bölümünden kalan (% işlemi)
    onlar1 = sayi1 // 10
    birler1 = sayi1 % 10
    onlar2 = sayi2 // 10
    birler2 = sayi2 % 10

    # Bulunan basamaklar ekrana yazdırılır
    print(sayi1, "-> onlar basamağı:", onlar1, ", birler basamağı:", birler1)
    print(sayi2, "-> onlar basamağı:", onlar2, ", birler basamağı:", birler2)

    # Ortak rakamlar bu listede toplanacak
    ortak = []

    # Birinci sayının her rakamı, ikinci sayının rakamlarıyla karşılaştırılır
    for rakam in [onlar1, birler1]:
        # Rakam ikinci sayıda varsa ve daha önce eklenmediyse listeye eklenir
        # (örneğin 11 ile 15'te 1 rakamı iki kez yazılmasın diye)
        if (rakam == onlar2 or rakam == birler2) and rakam not in ortak:
            ortak.append(rakam)

    # Liste boş değilse ortak rakamlar yazdırılır, boşsa uyarı verilir
    if len(ortak) > 0:
        print("Ortak rakamlar:", *ortak)
    else:
        print("Ortak rakam yoktur.")
