import urllib.request
import urllib.parse
import  urllib.error
import json
import random
import re
from bs4 import BeautifulSoup

def main():
    keyword = '猪八戒'
    keyword = urllib.parse.urlencode({"word":keyword})
    url = 'https://baike.baidu.com/search/word?%s' % keyword

    print(url)
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    for each in soup.find_all(href=re.compile("view")):
        # print(each.text , "->", ''.join(["http://baike.baidu.com",each["href"]]))
        content = ''.join([each.text])
        keyword2 = each["href"]
        print(keyword2)
        # keyword2 = str(keyword2)
        keyword21 = keyword2.split('=')[0]
        keyword22 = keyword2.split('=')[1]
        print(keyword21)
        print(keyword22)
        keyword23 = urllib.parse.quote(keyword22)
        keyword2 = keyword21+"="+keyword23
        print(keyword2)
        # url2 = ''.join(["http://baike.baidu.com", each["href"]])
        url2 = ''.join(["http://baike.baidu.com", keyword2])
        print(url2)
        reponse2 = urllib.request.urlopen(url2)
        html2 = reponse2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        print(content)
if __name__ == '__main__':

    main()





