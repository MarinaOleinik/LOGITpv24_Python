#1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine,
    - - lahutamine
    * - korrutamine
    / - jagamine
    Kui sisend ei ole järjendis [+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisesnd ujukomaarvu tüübina
    :param float arv2: Sisesnd ujukomaarvu tüübina
    :param str tehe: Sisend listist [+,-,/,*]
    :rtype: var Määramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
    :param int aasta:Sisend kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(külg:float)->any:
    """Kirjeldage funktsioon
    :param ...:...
    :rtype:...S,P,d
    """
    S=külg**2
    P=4*külg
    d=(2)**(1/2)*külg
    return S,P,d
#4
def season(param:int)->str:
    """Kirjeldage funktsioon
    :param ...:...in range(1,13)
    :rtype:...Hooajanimetus
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H
#5
def bank(summa:float, aastad:int)->float:
    """Kirjeldage funktsioon
    :param ...:...
    :param ...:...
    :rtype:...Hooajanimetus
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa
from random import *
#6
def is_prime(a=randint(1,10000))->bool:
    """Kirjeldage funktsioon
    :param ...:...
    :param ...:...
    :rtype:...
    """
    print(a)
    v=True 
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v
#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    """
    if päev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v