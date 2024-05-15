import requests
from ping3 import ping
'''
def get_gip():
    global gip
    try:
        gip = requests.get('http://api.ipify.org/')
        #print(gip.text)
    except requests.exceptions.RequestException as e:
        print("noconnection")
'''

class main():
    def __init__(self,gip=None,gip2=None):
        self.gip = gip 
    def get_gip(self):
        target = 'example.com' 
        result = ping(target)

        if result == False:
            gip="No Internet Connection"
            print(gip)
        else:
            gip = requests.get('http://api.ipify.org/')
            print(gip.text)
        
        '''
        try:
            gip = requests.get('http://api.ipify.org/')
        except requests.exceptions.RequestException as e:
            print("No Internet Connection")
        '''
my_global_ip = main()
my_global_ip.get_gip()