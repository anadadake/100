import urllib.request
import urllib.parse
import  urllib.error
import json
import random

if __name__ == '__main__':
    url  = 'http://whatismyip.com.tw/'

    iplist = '121.10.1.181:8080;115.223.221.158:9000;211.159.171.58:80;113.57.97.226:808;122.243.13.89:9000;115.223.229.45:9000;121.10.1.180:8080'.split(';')
    print(iplist)

    for a in iplist:
        # ip = random.choice(iplist)
        ip = a
        proxy_suppport = urllib.request.ProxyHandler({'http':ip})
        opener = urllib.request.build_opener(proxy_suppport)
        opener.addheaders= ['User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36']
        try:
            print('trying ip %s ...'%ip)
            response = urllib.request.urlopen(url)
        except urllib.error.URLError:
            print('Except occurred. ')
        else:
            print('Success!')





