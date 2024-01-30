#import requests
#responce = requests.get("https://coinmarketcap.com/ ")
##print(responce.text)

#responce_text = responce.text
#responce_parse = responce.text.split('<span>')
#for p_e1 in responce_parse:
#    if p_e1.startswith('$'):
#        for p_e2 in p_e1.split('</span>'):
#            if p_e2.startswith("$") and p_e2[1].isdigit():
#               print(p_e2)

import requests
from bs4 import BeautifulSoup

url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
soup_list_name = soup.find_all('a',{'class':"short-img img-fit"})

f = open("1.txt","a")

for a in soup.find_all('a', href=True):
    u = a['href']
    if u.startswith("http"):
        requst = requests.get(u)
        soup1 = BeautifulSoup(requst.text, features="html.parser")
        soup_list_name = soup1.find_all('span',{'class':'oname_ua'})
        if len(soup_list_name)>0:
            f.write(f"{soup_list_name[0].text}\n")
        soup_list_ul = soup1.find_all('ul', {'class': 'short-list fx-1'})
        for i in soup_list_ul:
            f.write(f'{i.text}\n')
f.close()



#f = open("1.txt","a")
#for name in soup_list_name:
    #f.write(f"{name.text}\n")
    #print(name.text)
#f.close()
