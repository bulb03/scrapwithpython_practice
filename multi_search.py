import requests
from bs4 import BeautifulSoup


url = "https://www.yelp.com/search?find_loc=London&start="
current_data = 0
loc = "London"
yelp = "yelp"
file_path = "{yelp}-{location}.txt".format(location=loc, yelp=yelp)
writeinto = open(file_path, "a")

while current_data < 50:
    scrap = requests.get(url + str(current_data))
    scrap_data = BeautifulSoup(scrap.text, "html.parser")
    search = scrap_data.findAll('div', {'class': 'biz-listing-large'})

    for i in search:
        title = i.findAll('a', {'class': 'biz-name'})[0].text,
        address = i.findAll('address')[0].text,
        phone = i.findAll('span', {'class': 'biz-phone'})[0].text
        wrote_data = "{title}\n{address}\n{phone}\n".format(
            title=title,
            address=address,
            phone=phone
        )

    writeinto.write(wrote_data)
    current_data += 10
