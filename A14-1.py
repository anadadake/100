import urllib.request

if __name__ == '__main__':
    html = urllib.request.urlopen('http://www.fishc.com').read().decode('utf-8')
    # html = response.read()
    print(html)
    print(type(html))

    response = urllib.request.urlopen('http://placekitten.com/g/200/300')
    print(type(response))
    print(response.geturl())
    print(response.info())
    print(response.getcode())
    cat_img = response.read()
    with open ('cat.jpg','wb') as f:
        f.write(cat_img)