from pprint import pprint
import requests
from bs4 import BeautifulSoup 
def dolar():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    t=(data['Valute']['USD'])
    a=(t["Value"])
    return a
print(dolar())

def anecdot():
    ren=requests.get("https://www.anekdot.ru/random/anekdot/")
    soup=BeautifulSoup(ren.text,"lxml")
    k=soup.find_all("div",class_="text")
    a=[]
    for i in k:
        a.append(i.text)
    return a

def nowos():
    ren=requests.get("https://www.interfax.ru/news/")
    soup=BeautifulSoup(ren.text,"lxml")
    k=soup.find_all("h3",class_="")
    s=[]
    for i in k:
        s.append(i.text)
    return s




