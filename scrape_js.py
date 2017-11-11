# 此檔案可以直接呼叫瀏覽器而不只是爬蟲而已

# 有關selenium.common.exceptions.WebDriverException: Message: 'geckodriver'...的問題
# 解法：http://blog.csdn.net/z_johnny/article/details/74540712

# 如果在ide而不是cmd裡執行python程式碼時，出現selenium.common.exceptions.WebDriverException: Message: Failed to decode response...
# 將selenium的webdriver檔放進python檔的資料夾裡；像此檔案要在vs code執行時，就要在其所屬資料夾scrap中放入：geckodriver.exe
# 根據瀏覽器不同而會有不一樣的檔案，edge的就叫做MicrosoftWebDriver.exe
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import shutil
import requests

url = "http://www.chrisburkard.com/"

# 啟動想起動的瀏覽器 #注意：根據你想啟動的瀏覽器，除了webdrive.瀏覽器名()不一樣外，你也要到selenium去下載和欲開啟的瀏覽器相關的檔案
#wd = webdriver.Edge()
wd = webdriver.Firefox()

# 連上想連的網站，跟requests.get的功能一樣
wd.get(url)
# 透過js抓取網站原代碼
html = wd.execute_script("return document.documentElement.outerHTML")

# 再用BeautifulSoup整理
web_soup = BeautifulSoup(html, 'html.parser')
# print(web_soup.text)
# 抓想抓的tag
image = web_soup.findAll('img')
length = len(image)
num = 0

while num < length:
    try:
        for i in image:
            # 抓img中的src
            a = i["src"]
            # 開啟圖片網址
            img_r = requests.get(a, stream=True)
            # 檔案的命名
            file_name = os.path.basename(a)
            # file_的檔案位置為：os.getcwd()+名為image的folder+file_name
            file_ = os.path.join(os.getcwd(), "image", file_name)
            with open(file_, "wb") as output:
                # 將讀到的img_r複製到file_的複製檔:"output"裡
                shutil.copyfileobj(img_r.raw, output)
            del file_
        # 讓他跑一下，才能下載完
        time.sleep(5)
    except:
        # 有時會有不能讀的網址，直接略過
        pass
    num += 1

print("finish")
