#https://myaccount.google.com/apppasswords Rakenduste paroolid
from http import server
from multiprocessing import context
import smtplib,ssl
from email.message import EmailMessage
import imghdr
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<h2>Sending an HTML email from Python</h2>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="oleinik.marina@gmail.com"
    parool=input("Rakenduste parool") #"agtd qnqq nrkc uotf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri,subtype="html")
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    with open("coconut.png","rb") as f:
        pilt=f.read()  
    msg.add_attachment(pilt,maintype="image",subtype=imghdr.what(None, pilt),filename="coconut.png")
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
        k,v=rida.strip()
        jarjend.append(v)
    f.close()
    return jarjend
import ast
def Loe_failist_1(fail:str)->list:
    with open('loetelu.txt', 'r', encoding='utf-8-sig') as f:
        for rida in f:
            rida = rida.strip()
            if rida:  # Kui rida ei ole tühi
                andmed=eval(rida)
                vaartused = list(andmed.values())
                print(vaartused)
    
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

loetelu=Loe_failist_1('Loetelu.txt')
print(loetelu)
# for i in range(8,11,1):
#     loetelu.append(input(f"{i}-i:"))
# Kirjuta_failisse('Loetelu.txt',loetelu)
# loetelu=Loe_failist('Loetelu.txt')
# print(loetelu)