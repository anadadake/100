from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/%E7%8C%AA%E5%85%AB%E6%88%92/769'
    response1 = urllib.request.urlopen(url)
    html = response1.read()
    # decode_html = html.decode('UTF-8')
    # print(decode_html)

    soup = BeautifulSoup(html,'html.parser')
    # print(soup)

    print(soup.title)
    print(soup.title.string)
    print(soup.title.parent.parent.name)
    print(soup.p)
    print(soup.p['class'])
    print(soup.a)
    # print(soup.find_all('a'))
    # print (soup.find_all(id='j-pinyin-speak'))

    for x in soup.find_all('a'):
        print(x)
        print(x.get('href'))