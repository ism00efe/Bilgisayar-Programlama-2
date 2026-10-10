# Soru 2: N sayısı kadar yıldızı yan yana yazdıran program

# Kullanıcıdan yazdırılacak yıldız sayısı alınır
n = int(input("N sayısını giriniz: "))

# Döngü N kez çalışır ve her seferinde bir yıldız yazdırır
for i in range(n):
    # end="" sayesinde alt satıra geçilmez, yıldızlar yan yana yazılır
    print("*", end="")

# Döngü bittikten sonra imleç alt satıra geçirilir
print()
