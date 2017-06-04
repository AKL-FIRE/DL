import requests

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Error'

if __name__ == '__main__':
    url = 'http://www.icourse163.org/home.htm'
    print(getHTMLText(url))