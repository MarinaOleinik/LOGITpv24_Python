from datetime import *
from calendar import *
from math import *
from time import strptime
#Ülesanne 10
minutid_kasutajalt=int(input("Aeg minutides:"))
tunnid=minutid_kasutajalt//60 # täisosa
minutid=minutid_kasutajalt%60 # jääk
print("vastus".center(20,"*")) # vorminda ise vastus nii: "hh:mm"

#Ülesanne 7,8,9 ise
#Ülesanne 6
t="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(t.upper())

#Ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(2*a,b,2*a,b,4*a)
#Ülesanne 4
#ise

#Ülesanne 3

try:
    R=float(input("Sisesta R,kus R on ringi raadius:"))
    # ==, !=, <, >, <=, >=
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        Ringi_S=round(pi*R**2,2)
        Ringi_P=round(2*pi*R,2)
        Ruudu_S=2*R*2*R
        Ruudu_P=4*2*R
        print(f"Ringi_S= {Ringi_S}\nRingi_P= {Ringi_P}\nRuudu_S= {Ruudu_S}\nRuudu_P= {Ruudu_P}")
except:
    print("Sisesta ainult arvud!!!")





tana=date.today()
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)

päev=tana.day
print(päev)
kuu=tana.month
aasta=tana.year

print(f"Päev on {päev},\nKuu on {kuu},\nAasta on {aasta}")
paevad=monthrange(2025,2)[1]
onjaanud=paevad-päev
print(f"Kuu lõpuni on jäänud {onjaanud} päevad")
try:
    sünnipäev=input("Sünnipäev: ") #YYYY-MM-DD
    sp=datetime.strptime(sünnipäev,"%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12
    print(f"Vastus: Vanus {vanus_aastades} aastad")
except:
    print("Sa pead YYYY-MM-DD format kasutada sisestamisel.")

#Ülesanne 2
#Sulgude kasutamine
print("a=3 + 8/ (4 - 2) * 4")
a=3 + 8 / (4 - 2) * 4
print(a)
print("a=(3 + 8)/ (4 - 2) * 4")
a=(3 + 8) / (4 - 2) * 4
print(a)
