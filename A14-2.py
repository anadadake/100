import urllib.request
import urllib.parse
import json

if __name__ == '__main__':
    url = 'https://www.convertstring.com/zh_CN/EncodeDecode/UrlDecode'
    data = {}
    data['input'] = '%E6%B5%8B%E8%AF%95'
    data['outputtype'] = 'outputstring'

    # header = {}
    # header['Referer']='http://fanyi.youdao.com/'
    # header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    # data['type'] = 'AUTO'
    # data['i'] = '测试'
    # data['doctype'] = 'json'
    # data['xmlVersion'] = '1.6'
    # data['keyfrom'] = 'fanyi.web'
    # data['ue'] = 'UTF-8'
    # data['typoResult'] = 'true'
    # data['from'] = 'AUTO'
    # data['to'] = 'AUTO'
    # data['smartresult'] = 'dict'
    # data['client'] = 'fanyideskweb'
    # data['salt'] = '1529934028755'
    # data['sign'] = '792433acc8b642df2d37a6338ba33346'
    # data['doctype'] = 'json'
    # data['version'] = '2.1'

    # data['action'] = 'FY_BY_REALTIME'

    # data['i'] = '测试'
    # data['from'] = 'AUTO'
    # data['to'] = 'AUTO'
    # data['smartresult'] = 'dict'
    # data['client'] = 'fanyideskweb'
    # data['salt'] = '1529935597435'
    # data['sign'] = 'dd11e6fd4f7857136a7f5c3fd5c93ebc'
    # data['doctype'] = 'json'
    # data['version'] = '2.1'
    # data['keyfrom'] = 'fanyi.web'
    # data['action'] = 'FY_BY_REALTIME'
    # data['typoResult'] = 'false'

    data = urllib.parse.urlencode(data).encode('utf-8')

    # response = urllib.request.urlopen(url, data)

    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    print(html)
    # a = json.loads(html)
    # print(type(a))
    # print(a.keys())
