import json
import urllib.request

client_id = "<CLIENT ID>"
client_secret = "<CLIENT SECRET>"


def translateKRToEN(name):
    encText = urllib.parse.quote(str(name))
    url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode == 200):
        response_body = response.read()
        json_dict = json.loads(response_body.decode('utf-8'))
        result = json_dict['aResult'][0]
        name_items = result['aItems']
        names = [name_item['name'] for name_item in name_items]
        return names[0]
    else:
        print("Error Code:" + rescode)
