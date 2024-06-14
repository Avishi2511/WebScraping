import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")
headers = table.find_all("th")

titles = []
for i in headers:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns = titles)

rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("ipl.csv")

#text.strip()->used to remove symbols and get only the text
# strip()> whichever value needs to be removes can be put in (), by default \n or space
#changes made in row code since 1st column values (team) wasn't visible because of \n present in code