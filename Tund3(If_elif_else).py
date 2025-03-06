# #Näidised
# #Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#     print(f"Korrutis võrdub: {a*b}")

# #Kas a on paaris või paaritu arv?
# if a%2==0 and a!=0:
#     print(f"Arv {a} on paaris")
# elif a==0:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"Arv {a} on paaritu")

# #Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("Mis hinne sai täna koolis?"))
#     if hinne in range(1,6):
#         print("Hinne")
#         if hinne==5:
#             print("VH")
#         elif hinne==4:
#             print("H")
#         elif hinne==3:
#             print("R")
#         else:
#             print("MR")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga:", e)

nimi="PYTHON"
print(nimi.isupper())
if nimi.isupper():
    print("Suured tähed")
else:
    print("Ei ole kõik suured tähed")
#Ülesanne
#1 Juku
nimi=input("Mis on sinu nimi?")
if nimi=="JUKU":
    print("Lähme kinno!")
    vanus=int(input("Kui vana sa oled?"))

else:
    print("Ma olen hõivatud! Mine kinno ise!")

#2 Pinginaabrid
# Ilja Aleksei Marina, Aleksei Ilja Marina,....
nimed=["Ilja","Aleksei","Marina"]
nimi1=input()
nimi2=input()
nimi3=input()
if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
    print("Pinginaabrid")
else:
    print("Ei ole pringinaabrid")

#3 Remont
#--------
a=float(input("Pikkus: "))# kontroll
b=float(input("Laius: "))
#--------
S=a*b
soov=input("Kas tahad remondi teha?")
if soov.lower()=="jah":
    print("Remont")
    #---------
    hind=float(input("Hind: ")) # kontroll
    #---------
    koguhind=S*hind
    print(f"Sul on vaja {koguhind} Eur")
else:
    print("Head aega!")