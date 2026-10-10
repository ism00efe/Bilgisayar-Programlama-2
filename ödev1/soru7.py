# Soru 7: P(x, y) noktasının y = m*x + n doğrusu üzerinde olup olmadığını kontrol eden program

# Kullanıcıdan noktanın koordinatları alınır
x = float(input("Noktanın x koordinatını giriniz: "))
y = float(input("Noktanın y koordinatını giriniz: "))

# Kullanıcıdan doğru denkleminin katsayıları alınır
m = float(input("Doğrunun m katsayısını giriniz: "))
n = float(input("Doğrunun n katsayısını giriniz: "))

# Nokta doğrunun üzerindeyse y = m*x + n eşitliği sağlanır
if y == m * x + n:
    print("P(", x, ",", y, ") noktası doğrunun üzerindedir.")
else:
    print("P(", x, ",", y, ") noktası doğrunun üzerinde değildir.")
