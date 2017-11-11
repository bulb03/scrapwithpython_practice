# 抓bing wallpaper 的爬蟲
# 設定好基本url和變數 -> requests.get json檔的位址 -> 用json.loads抓json檔的內容
# 讀取json檔中的startdate(作為檔名)和url(圖片實際位址)並各自放入file_name和target中
# 利用while loop來跑(因為要多張)，步驟請至47行觀看

import requests
import json
import os
import shutil
import time


# 讀到的圖片url要接上basic_url才會獨自開啟圖片url
basic_url = "https://bing.com"

# 背景圖片的json檔位址(n是要查詢的數量)
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-tw"

# 要傳去接url的變數(因為我想抓很多張，所以就用list)
target = []

# 新檔案名稱(因為我想抓很多張，所以就用list)
file_name = []


# 連上json檔位址
data = requests.get(url)

# 讀取json檔的內容
jsondata = json.loads(data.text)


# jsondata是list，我們只要讀圖片的url
for i in jsondata['images']:
    if(i['startdate'] != None):
        file_name.append(i['startdate'] + ".jpg")
    if(i['url'] != None):
        # 得到該圖片的url
        target.append(basic_url + i['url'])
    else:
        pass


j = 0
# bing的一次最多8張，所以讓他跑8次
while j < 8:
    # 開啟該圖片
    download = requests.get(target[j], stream=True)
    # 準備空白檔案，複製進去
    file_ = os.path.join(os.getcwd(), "image", file_name[j])

    with open(file_, "wb") as output:
        shutil.copyfileobj(download.raw, output)
        del file_
    time.sleep(3)
    j += 1
