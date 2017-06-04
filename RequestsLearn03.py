import requests
print('Input ip:')
ip = raw_input()
try:
    r = requests.get('http://www.ip138.com/ips138.asp?ip=' + ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('Error')
