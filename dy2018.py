from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import datetime

# Step 1: 处理index页面，获取全部2级栏位和对应的页面url
# Step 2：循环2级栏位，循环页面，获取电影名称和下载的url，保存成csv

index_url = 'https://www.dy2018.com'
now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
csv_file_name= ''.join([now_time, '_csv' ,'.txt'])

def process_magnet_link(url, title):
    sub_response = urllib.request.urlopen(url)
    sub_soup = BeautifulSoup(sub_response.read(), 'html.parser')
    magnet_url = sub_soup.find(href=re.compile('^magnet'))
    if magnet_url != None and magnet_url.text != None and title != None:
        return magnet_url.text + ',' + title
    else:
        return 'error: no valid magnet url in ' + url + "," + title

if __name__ == '__main__':
    print('Author Kevin on 2018-06-29.')
    print('Starting to get movie magnet url from https://www.dy2018.com ...')
    # print(csv_file_name)
    # print(type(csv_file_name))
    response = urllib.request.urlopen(index_url)
    index_html = response.read()

    soup = BeautifulSoup(index_html, 'html.parser')
    sub_htmls = soup.find_all('a', href=re.compile('^/i/\d*\.html'))
    with open(csv_file_name, 'w', encoding='utf-8') as output_file:
        for i in sub_htmls:
            sub_url = index_url + i.attrs.get('href')
            title = i.attrs.get('title')
            dl_link_with_title = process_magnet_link(sub_url, title)
            print(dl_link_with_title)
            #output_file.writelines(index_url + i.attrs.get('href') + ',' + i.attrs.get('title') + '\n')
            output_file.writelines(dl_link_with_title + '\n')

    print(''.join(['Finshed. Please refer to file ',csv_file_name]))
    print(' :) orz. Enjoy the movie.')