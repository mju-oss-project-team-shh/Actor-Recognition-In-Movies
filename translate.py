import json
import urllib
from urllib import parse
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

baseUrl = "https://openapi.naver.com/v1/krdict/romanization?query="
client_id = "2SULrTwEBG_Y1J6zzlKw"
client_secret = "PNxbkrEUFt"
ssl._create_default_https_context = ssl._create_unverified_context


def translateKRToEN(name):
    spNames = name.split(" ")
    tNames = []
    for n in spNames:
        encText = parse.quote(n)
        url = baseUrl + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode == 200):
            response_body = response.read()
            json_dict = json.loads(response_body.decode('utf-8'))
            print(json_dict)
            result = json_dict['aResult'][0]
            name_items = result['aItems']
            names = [name_item['name'] for name_item in name_items]
            tNames.append(names[0].replace(" ", "_"))
        else:
            print("Error Code:" + rescode)
    return ' '.join(tNames)


