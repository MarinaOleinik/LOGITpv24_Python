#https://myaccount.google.com/apppasswords Rakenduste paroolid
from http import server
from multiprocessing import context
import smtplib,ssl
from email.message import EmailMessage
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="Tere, see on test"
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="oleinik.marina@gmail.com"
    parool=input("Rakenduste parool") #"agtd qnqq nrkc uotf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga:",e)
    finally:
        server.quit()

def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

loetelu=Loe_failist('Loetelu.txt')
print(loetelu)
for i in range(8,11,1):
    loetelu.append(input(f"{i}-i:"))
Kirjuta_failisse('Loetelu.txt',loetelu)
loetelu=Loe_failist('Loetelu.txt')
print(loetelu)