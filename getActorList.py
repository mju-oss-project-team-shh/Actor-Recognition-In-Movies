import urllib.request
from urllib.parse import quote
import json
import requests
 
naver_client_id = "YQnqDgyeE_zZHVYQz06E"
naver_client_secret = "prAUDxEPTz"

 # title :the title of a movie to search for actors
def searchByTitle(title):
    #use Naver API
    url = 'https://openapi.naver.com/v1/search/movie.json?query=' + quote(title)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    #when API usage is successful
    if(rescode==200):
        response_body = response.read()
        data = response_body.decode('utf-8')
        jsonresult = json.loads(data)
        
        #find appropriate movie in search results

        for item in jsonresult['items']:
            
            if(item['title'] == '<b>'+title+'</b>'):
                #extracting actor list
                actors = item['actor'].split('|')
                return actors
        return []
        
    
    #API usage error
    else:
        print("Error Code:" + rescode)
 

