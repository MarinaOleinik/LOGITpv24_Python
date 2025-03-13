#4
päev=int(input("Sünnipäev"))
kuu=int(input("Sünnikuu"))
if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
    märk="Jäär"
elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
    märk="Sõnn"

print(märk)
#3
try:
    soov=input("Kas tahad dekodeerida?").lower()
    if soov=="jah":
        try:
            nr=int(input("Päeva number: "))
            if nr in range(1,8):
                if nr==1:
                    print("Esmaspäev")
                elif nr==2:
                    print("Teisipäev")
            else:
                print("Ainult 1-7")
        except:
            print("Numbrid vahemikust 1-7")
except:
    print("Mul on vaja vastus Jah või Ei")


#2
try:
    nurk1=float(input("Esimene nurk"))
    nurk2=float(input("Teine nurk"))
    nurk3=float(input("Kolmas nurk"))
    if nurk1>0 and nurk2>0 and nurk3>0:
        print("Nurgad on positiivsed")
        if nurk1+nurk2+nurk3==180:
            print("See on kolmnurk")
            if nurk1==nurk2 and nurk2==nurk3:
                print("Võrdkülgne kolmnurk")
            elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
                print("Võrdvaarne kolmnurk")
            else:
                print("Erikülgne kolmnurk")
        else:
            print("See ei ole kolmnurk")
    else:
        print("Negatiivsed nurgad ei soobi")
except:
    print("Sisesta ujukomaarvud")


#1
try:
    arv=input("Sisesta arv:")
    if arv.isnumeric():
        arv=int(arv)
        if arv>0:
            if arv%2==0:
                print("Paaris arv")
            else:
                print("Paaritu")
        else:
            print("Negatiivne arv")
except:
    print("Kirjuta numbreid")
