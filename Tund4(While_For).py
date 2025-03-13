


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