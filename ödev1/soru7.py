# Soru 7: P(x, y) noktasının y = m*x + n doğrusu üzerinde olup olmadığını kontrol eden program

x = float(input("Noktanın x koordinatını giriniz: "))
y = float(input("Noktanın y koordinatını giriniz: "))
m = float(input("Doğrunun m katsayısını giriniz: "))
n = float(input("Doğrunun n katsayısını giriniz: "))

if y == m * x + n:
    print("P(", x, ",", y, ") noktası doğrunun üzerindedir.")
else:
    print("P(", x, ",", y, ") noktası doğrunun üzerinde değildir.")
