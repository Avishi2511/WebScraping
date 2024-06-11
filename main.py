#requests lib is used to get the HTTP of any website

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

#print(r.status_code)
# status code is used to determine the status of website i..e used to indicate whether specific HTTP request successful or not (check MDN docs)
#print (r.text)

soup = BeautifulSoup(r.text,"lxml")
#print(soup)
#print(soup.div) #will only print the div tags

#to get navigable strings from html
#tag = soup.div.p.string
#print(tag)


#functions
#find() -> used to find the first requested tag in the code
'''
price=(soup.find("h4",{"class":"price float-end card-title pull-right"}))
print(price.string)
desc = (soup.find("p", {"class":"description"}))
print(desc.string)
a=(soup.find("p",class_="description"))
print(a.string)
'''

#find_all()->used to find all the tags that is requested
'''
prices = soup.find_all("h4", class_ ="price float-end card-title pull-right")
print(len(prices))

for i in prices:
    print(i.string)

desc = soup.find_all("p", class_ = "description")
print(desc[3].string)
'''

import re
#data = soup.find_all(string = "Galaxy Tab 3")
data = soup.find_all(string = re.compile("Idea"))
print(data)
