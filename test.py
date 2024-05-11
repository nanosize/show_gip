import requests

def get_gip():
    global gip
    try:
        gip = requests.get('http://api.ipify.org/')
        #print(gip.text)
    except requests.exceptions.RequestException as e:
        print("noconnection")
get_gip()
print(gip.text)