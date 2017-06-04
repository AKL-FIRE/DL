import requests
print('What do you want to search?')
keyword = raw_input()
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    r.raise_for_status()
    print(len(r.text))
except:
    print('Error')

