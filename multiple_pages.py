#flipkat website
#we use the buttons for going to next page at the bottom
import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
for i in range(2,11):
    url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    np = soup.find("a", class_ = 'cn++Ap').get("href")
    cnp = "https://www.flipkart.com"+np
    print(cnp)
'''

Names = []
Prices = []
Desc = []
Reviews = []

for i in range(1,11):
    url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")

    names = box.find_all("div", class_="KzDlHZ")
    for i in names:
        n = i.text
        Names.append(n)

    prices = box.find_all("div", class_ = "Nx9bqj _4b5DiR")
    for i in prices:
        n = i.text
        Prices.append(n)

    desc = box.find_all("ul", class_ = "G4BRas")
    for i in desc:
        n = i.text
        Desc.append(n)

    reviews = box.find_all("div", class_ = "XQDdHH")
    for i in reviews:
        n = i.text
        Reviews.append(n)

df = pd.DataFrame({"Product_name":Names, "Product Prices":Prices, "Product Description":Desc, "Reviews":Reviews})
df.to_csv("multiples_pages.csv")
