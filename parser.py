import requests
responce = requests.get("https://coinmarketcap.com/ ")
#print(responce.text)

responce_text = responce.text
responce_parse = responce.text.split('<span>')
for p_e1 in responce_parse:
    if p_e1.startswith('$'):
        for p_e2 in p_e1.split('</span>'):
            if p_e2.startswith("$") and p_e2[1].isdigit():
                print(p_e2)

