from math import *
#----------------------
print("Ruudu karakteristikud")
try:
    a=int(input('Sisesta ruudu k�lje pikkus => '))
    if a>0:
        S=a**2
        print(f"Ruudu pindala, {S}")
        P=4*a
        print(f"Ruudu �mberm��t {P}")
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
    else:
        print("K�lg ei saa olla <=0-ga")
except:
    print("K�lje suurus on vaja int formaadis sisestada!")
#----------------------
print("Ristk�liku karakteristikud")
b=int(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c=int(input("Sisesta ristk�liku 2. k�lje pikkus => "))
if b>0 and c>0:
    S=b*c
    print(f"Ristk�liku pindala', {S}")
    P= 2 *(b+c)
    print(f"Ristk�liku �mberm��t, {P}")
    di=sqrt((b**2)+(c**2))
    print("Ristk�liku diagonaal", round(di))
#-------------------
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print(f"Ringi l�bim��t {d}")
S=pi*r**2
print("Ringi pindala", round(S))
C=2*pi*r
print("Ringjoone pikkus", round(C))