from colorama import *
init(autoreset=True)
print(Fore.RED + "See on punane tekst")
print(Back.GREEN + "See on roheline taust")
print(Style.BRIGHT + "Heledam (bold) tekst")
print(Fore.YELLOW + Back.BLUE + "Kombineeritud värvid")



from random import *
sõnad=["arvuti","hiir","kuvar"]
salasõna=choice(sõnad)
print(salasõna)
k=len(salasõna)
p=6
while p>0:
    print("_ "*k)
    print(f"On jäänud {p} katset")
    p-=1
    sõna=input("Sisesta oma variant: ").lower()
    if sõna==salasõna: 
        print("Huraa!")
        break
    else:
        pass