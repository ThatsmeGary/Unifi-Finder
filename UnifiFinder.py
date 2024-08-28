import requests
from os import system
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint


requests.urllib3.disable_warnings(InsecureRequestWarning)


def clean():
    return system("cls")
    

LISTA_SITES = list()
FOUND_MAC = False
URL = "https://YOUR_URL_SITE_OR_LINK/api/login"

headers = {"Accept":"application/json",
          "Content-Type": "aplication/json"}

credentials = {"username": "YOUR_USERNAME",
               "password": "YOUR_PASSWORD"}

# Abre uma sessão com o site da UNIFI
with requests.Session() as session:
    session.post(url=URL, json=credentials, headers=headers, verify=False)  
    
    clean()
    print("ENTER THE MAC ADDRESS OF THE DEVICE YOU WANT TO FIND: ")
    MAC = str(input("PUT MAC ADDRESS WITH 2 DOTS (:) ==> ")).lower()
    
    URLS = session.get(url="https://YOUR_URL_SITE_OR_LINK/api/self/sites").json()
        
    for x in URLS['data']:
        LISTA_SITES.append(x['name'])
    
    for x in LISTA_SITES:    
        # Recupera o nome do site
        name_site = ''
        
        for name in URLS['data']:
            if name['name'] == x:
                name_site = name['desc']
                break
        
        
        # Recupera o MAC do dispositivo   
        sites = session.get(url=f"https://YOUR_URL_SITE_OR_LINK/api/s/{x}/stat/device").json()
        
        for mac in sites['data']:
            if mac['mac'] == MAC:
                print()
                print(f"I found MAC on the website {name_site}")
                print()
                input("Press [ENTER] to leave the script ")
                FOUND_MAC = True
                break  
                
if not FOUND_MAC: 
    print()        
    print("I DIDN'T FIND ANY ASSOCIATED MAC.")
    input("Press [ENTER] to leave the script ")
    clean()
