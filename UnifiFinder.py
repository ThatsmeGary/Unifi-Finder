import requests
from urllib3.exceptions import InsecureRequestWarning


requests.urllib3.disable_warnings(InsecureRequestWarning)

LIST_SITES = list()
FOUND_MAC = False
URL = "https://unifi.openinternet.net.br:8443/api/login"

headers = {"Accept": "application/json",
           "Content-Type": "aplication/json"}


USERNAME = input(str("USERNAME ==> "))
PASSWORD = input(str("PASSWORD ==> "))


credentials = f'"username": "{USERNAME}",\
                "password": "{PASSWORD}"'


# Open a session with the UNIFI website
with requests.Session() as session:
    session.post(url=URL, json=credentials, headers=headers, verify=False)

    print("ENTER THE MAC ADDRESS OF THE DEVICE YOU WANT TO FIND: ")
    MAC = str(input("PUT MAC ADDRESS WITH 2 DOTS (:) ==> ")).lower()

    URLS = session.get(
        url="https://unifi.openinternet.net.br:8443/api/self/sites").json()

    for x in URLS['data']:
        LIST_SITES.append(x['name'])

    for x in LIST_SITES:

        # Retrieves the site name
        name_site = ''

        for name in URLS['data']:
            if name['name'] == x:
                name_site = name['desc']
                break

        # Retrieves device MAC
        sites = session.get(
            url=f"https://unifi.openinternet.net.br:8443/api/s/{x}/stat/device").json()

        for mac in sites['data']:
            if mac['mac'] == MAC:
                print()
                print(f"I found MAC on the website {name_site}")
                FOUND_MAC = True
                break

if not FOUND_MAC:
    print("I DIDN'T FIND ANY ASSOCIATED MAC.")
