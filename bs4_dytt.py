from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import datetime

# Step 1: 处理index页面，获取全部2级栏位和对应的页面url
# Step 2：循环2级栏位，循环页面，获取电影名称和下载的url，保存成csv


index_url = 'https://www.dy2018.com'
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def process_magnet_link(url,title):
    sub_response = urllib.request.urlopen(url)
    sub_soup = BeautifulSoup(sub_response.read(), 'html.parser')
    magnet_url = sub_soup.find(href=re.compile('^magnet'))
    if magnet_url!=None and magnet_url.text !=None and title!=None:
        return magnet_url.text + ',' + title
    else:
        return 'error:' + url + "," + title

if __name__ == '__main__':

    response = urllib.request.urlopen(index_url)
    index_html = response.read()

    soup = BeautifulSoup(index_html, 'html.parser')

    # second

    sub_htmls = soup.find_all('a', href=re.compile('^/i/\d*\.html'))
    # with open('aaa.txt', 'w', encoding='utf-8') as output_file:

    for i in sub_htmls:
        # print(i)
        # print(index_url + i.attrs.get('href'))
        # print(i.attrs.get('title'))
        sub_url = index_url + i.attrs.get('href')
        title = i.attrs.get('title')
        print(process_magnet_link(sub_url,title))
        # output_file.writelines(index_url + i.attrs.get('href') + ',' + i.attrs.get('title') + '\n')

        # print(i.find())
        # sub_html = index_url+ Stri.href
        # print(i.href)

    # secondParentList = soup.find_all(class_='co_area2')
    # for second in secondParentList:
    #     print(second.a.text)

    # print(soup.prettify())
