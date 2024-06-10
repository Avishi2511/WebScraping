#requests lib is used to get the HTTP of any website

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)

#print(r.status_code)
# status code is used to determine the status of website i..e used to indicate whether specific HTTP request successful or not (check MDN docs)
#print (r.text)

soup = BeautifulSoup(r.text,"lxml")
#print(soup)
#print(soup.div) #will only print the div tags

#to get navigable strings from html
tag = soup.div.p.string
print(tag)




