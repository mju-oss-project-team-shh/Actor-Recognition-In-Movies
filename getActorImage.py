from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from selenium import webdriver
import os
import ssl
import asyncio

# Search and get image with google


def getActorImage(search):

    ssl._create_default_https_context = ssl._create_unverified_context
    url = f'https://www.google.com/search?q={quote_plus(search)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjU-KPJ1YjrAhWbZt4KHRvQDPUQ_AUoAXoECA0QAw&biw=1920&bih=925'

    path = "your chrome driver path"
    driver = webdriver.Chrome(path)
    driver.get(url)
    for i in range(500):
        driver.execute_script('window.scrollBy(0, 10000)')

    html = driver.page_source
    soup = BeautifulSoup(html)
    img = soup.select('.rg_i.Q4LuWd')

    n = 1
    imgurl = []

    for i in img:
        try:
            imgurl.append(i.attrs["src"])
        except KeyError:
            imgurl.append(i.attrs["data-src"])

    if os.path.isdir(path):
        print("이미 존재하는 배우입니다.")
    else:
        os.mkdir(path)
        for i in imgurl:
            path = f'./dataset/actors/{search}/'

            filename = '0000000' + str(n)
            print("파일이름" + filename)
            if(n > 9):
                filename = '000000' + str(n)
            urlretrieve(i, path + filename + ".jpg")
            n += 1
            print(str(n) + "번째 사진 저장 완료!")

            # 이미지 파일 갯수 70개 제한
            if(n == 70):
                break

            print(url)

        driver.close()
