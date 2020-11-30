from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from selenium import webdriver
import chromedriver_autoinstaller
import os
import ssl
import asyncio
from translate import translateKRToEN


# Search and get image with google
def getActorImage(search):

    chromedriver_autoinstaller.install()

    ssl._create_default_https_context = ssl._create_unverified_context
    url = f'https://www.google.com/search?q={quote_plus(search)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjU-KPJ1YjrAhWbZt4KHRvQDPUQ_AUoAXoECA0QAw&biw=1920&bih=925'

    driver = webdriver.Chrome()
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

    conv = translateKRToEN(search)
    path = f'./dataset/actors/{conv}/'
    if os.path.isdir(path):
        print("This actor's dataset already exists")
    else:
        os.mkdir(path)
        for i in imgurl:
            filename = '0000000' + str(n)
            print("파일이름" + filename)
            if(n > 9):
                filename = '000000' + str(n)
            urlretrieve(i, path + filename + ".jpg")
            n += 1
            print("Saved image #" + str(n))

            # 이미지 파일 갯수 40개 제한
            if(n == 40):
                break

            print(url)

        driver.close()

