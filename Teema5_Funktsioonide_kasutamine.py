sõnad=[]
for i in range(5):
    sõnad.append(input(f"{i+1}. sõna: "))
print(sõnad)


from Teema5_Kasutajate_fun import *
#try except!
a=float(input("Arv1:"))
b=float(input("Arv2:"))
t=input("Tehe:")
vastus=arithmetic(a,b,t)
print(vastus)

vastus=arithmetic(float(input("Arv1:")),float(input("Arv2:")),input("Tehe:"))
print(vastus)

#is_year_leap funktsiooni kasutamine
aasta=int(input("Mis aasta tahad kontrollida? "))
if aasta>0: 
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")

# square() kasutamine
#Kontroll while True ja try except...
a=float(input("Ruudu külg= "))

S,P,d=square(a)