from bs4 import BeautifulSoup
import requests
import pandas

urls = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=server&_sacat=0&_pgn="
l = []
for url in range(1,11,1):
    #print(urls+str(url))
    r = requests.get(urls+str(url))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"s-item__wrapper clearfix"})
    for item in all:
        d = {}
        d["Sever Details"]=item.find("h3",{"class":"s-item__title"}).text
        d["Server Price"]=item.find("span",{"class":"s-item__price"}).text
        #print(item.find("h3",{"class":"s-item__title"}).text)
        #print(item.find("span",{"class":"s-item__price"}).text)
        l.append(d)


df = pandas.DataFrame(l)

df.to_csv("Server_price.csv")
