import requests
from bs4 import BeautifulSoup

def load():
    url = "http://212.220.202.18/asp/Curriculum/Assignments.asp"

    payload='LoginType=0&AT=89863780261969872932870&VER=1644665187&MenuItem=0&TabItem=30&optional=optional'
    headers = {
    'Cookie': 'NSSESSIONID=996637802607930446258148; ASPSESSIONIDQSBSATQQ=MPBJIDJDOGFNLOHNGPJJAEFH; ASPSESSIONIDQSBQCSRQ=JIHBBBJDJFJILDNONCIGKLCG; TTSLogin=BSP=0&CN=3&SFT=2&SID=66&CID=2&PID=%2D1&SCID=1; ESRNSec=ESRNSECR1863162272=534496480%2D1896233664; ASPSESSIONIDQQBSDSRR=LDNHPPIDIAHDNDCIOPBKCDJB; ASPSESSIONIDQSBQCSRQ=HIHBBBJDJAKJCDEPNLKDJFGG; NSSESSIONID=996637802607930446258148',
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with open("index.html",'w',encoding="utf-8") as f:
        f.write(response.text)
        print(response.text)

arr = ["Английский язык","Речь и культура общения","Математика","Литературное чтение","Окружающий мир","Русский язык","Основы религиозных культур и светской этики","Физкультура","Технология","Изобразительное искусство","Музыка"]

def parse():
    with open("index.html",encoding="utf-8") as f:
        src = f.read()

    soup = BeautifulSoup(src,"lxml")
    table = soup.find("table",class_="table table-bordered table-thin table-xs print-block").find_all("tr",bgcolor="#FFFFFF")
    for i in table:
        if i.find("td",class_="text-center").text=="Д" and i.find("a",title="Смотреть подробности задания").text != "-":
            if i.find("td",class_="hidden-scr-sm") == None:
                print("%s : %s"%(i.find("td").text,i.find("a",title="Смотреть подробности задания").text))
            else:
                print("\n"+i.find("td").text+"\n")
                print("%s : %s"%(list(i.find("td").next_elements)[3].text,i.find("a",title="Смотреть подробности задания").text))

load()
