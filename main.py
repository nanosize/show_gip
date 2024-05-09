import requests 

#url = 'http://inet-ip.info/'
url = requests.get('http://api.ipify.org/') 
print(url.text)
#aaaa