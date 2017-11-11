# 步驟：
# request連結上該網頁->beautifulsoup去抓html代碼下來->使用者在輸入要查詢的東西


# requests是用來呼叫網頁的
import requests

# BeautifulSoup是python的一個庫，用來爬蟲，BeautifulSoup 4已被移到bs4，故須從bs4 import BeautifulSoup
from bs4 import BeautifulSoup

base_url = "https://www.yelp.co.uk/search?find_desc=Food&find_loc=London"
prod = "London"
search_data = base_url + prod
loc = "London"
yelp = "yelp"

# format介紹：前面的大括號就是要用來取代掉的，
# 例如：{location}裡的東西代表"一個叫location的大括號"，
# 在後面的format裡(location=loc)代表{location}會被變數loc取代，變數loc放的是"London"
# yelp以此類推；所以，file_path最後會等於"yelp-London.txt"
file_path = "{yelp}-{location}.txt".format(location=loc, yelp=yelp)

# 呼叫該網頁
scrap = requests.get(search_data)


# print(scrap) #通常會回覆status 200

# scrap.text用VS code的終端機是印不出來的，得要寫成print(scrap.text)才行，但挺漂亮的


# 取得網站原始碼
scrap_bs = BeautifulSoup(scrap.text, 'html.parser')


# 漂亮一點的html
# print(scrap_bs.prettify())

# 就是醜一點的html
# print(scrap_bs)

# 找要找的東西(通常是tag：a、div、class之類的)
# findAll會找的是那些class叫做"biz-listing-large"的div，所以會傳一堆div，這些div會以list儲存
data = scrap_bs.findAll('div', {'class': 'biz-listing-large'})

for i in data:
    #<div class='biz-listing-large'>底下包有很多tags，下面的範例是我們要找電話號碼和地址
    # print(i)就可以印出一組<div class='biz-listing-large'>

    # 存放電話的tag是<span class="biz-phone">
    phone = i.findAll('span', {'class': 'biz-phone'})

    # 存放地址的tag是<address>
    address = i.findAll('address')

    # 因為<div class='biz-listing-large'>裡只會有一組<span class="biz-phone">和<address>
    # 所以list只有存一個東西
    # print(phone[0].text, address[0].text)
    # print(phone[1].text, address[1].text) => 這行驗證了findAll傳回的list只有放一個東西

    # 寫進txt檔
    new_phone = phone[0].text
    new_address = address[0].text

    with open(file_path, "a") as textfile:
        pagedata = "{phone}\n{address}".format(
            phone=new_phone,
            address=new_address
        )
        textfile.write(pagedata)

    # 以下這堆是不想用上面方法卻想得到一樣結果的另一種方法
    #    for phone in i.findAll('span', {'class': 'biz-phone'}):
    #        print(phone.text)
    #        for address in i.findAll('address'):
    #            print(address.text)
