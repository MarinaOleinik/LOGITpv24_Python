from random import *
#7
N=1
for i in range(4):
    N*=10
    N+=randint(0,9)
    print(N)
#3
for küsimuse_nr in range(10):
    a=randint(1,50)
    b=randint(1,50)
    õige_vastus=a+b
    print(f"{a}+{b}", end="")
    p=0
    õ=0
    vastus=0
    while p<5 and vastus!=õige_vastus:
        vastus=int(input("="))
        if vastus==õige_vastus: 
            print("Tubli!")
            õ+=1
        p+=1
    print(f"Õige vastus: {õige_vastus}")
print("???????")



#5
N=int(input("N:" ))
for j in range(N):
    for i in range(N):
        if i==j or i==N-j-1:
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
print()
#2
summa=0
j=0
while True:
    while True:
        try:
            a=float(input("a: "))
            break
        except:
            print("viga!")
    summa+=a
    j+=1
    if j==10: break
print(f"Arvude summa: {summa}")
#-------
summa = 0
while True:
    number = input("Sisesta arv (vajuta Enter lõpetamiseks): ")
    if number == "": break
    try:
        number=float(number)
        summa += number 
    except:
        print("viga")   
print(f"Arvude summa: {summa}")


#Näidis:
# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# print()
# for i in range(0,10,1):
#     print(f"{i+1}. samm")
# print()
# for i in range(1,11):
#     print(f"{i}. samm")

#1
while True:
    try:
        nimi=input("Mis on sinu nimi? ")
        if nimi.isalpha(): break
    except:
        print("Viga!")
while True:
    try:
        k=int(input("Mitu korda tervitada? ")) #k.isnumeric()
        if k>0: break
    except:
        print("Viga!")
#1. variant
print("while True")
i=0
while True:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")
    if i==k: break
#3. variant
print("while tingimusega")
i=0
while i<k:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")
#3. variant
print("For")
for i in range(1,k+1):
    print(f"Ole tervitatud, {nimi}, {i}. korda.")