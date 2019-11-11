import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.businessrecord40.com/caroline-bettis'

# opeining up connection, grabbing page
uClient = uReq(my_url)
# puts content into variable
page_html = uClient.read()
#close web connection
uClient.close()

filename = "test3.csv"

# use if creating new file
f = open(filename, "w")

# use if adding to an existing file
#f = open(filename, "a")

header = "name, age, title, family, reason 40 under 40, motivation, fun fact\n"

# use only when writing a document otherwise comment out
f.write(header)

# html parsing
page_soup = soup(page_html, "html.parser")

# change ID for each person
content = page_soup.find("div",{"id":"block-7a5c1de9ad874ac39e2e"})

name_field = content.p.text

age_start = content.find_all('p')[1].text
index = age_start.find(':') + 2
age = age_start[index:]

title_start= content.find_all('p')[2].text
index = title_start.find(':') + 2
title = title_start[index:]

family_start = content.find_all('p')[3].text
index = family_start.find(':') + 2
family = family_start[index:]

reason_start = content.find_all('p')[4].text
index = reason_start.find(':') + 2
reason = reason_start[index:]

motivation_start = content.find_all('p')[5].text
index = motivation_start.find(':') + 2
motivation = motivation_start[index:]

fact_start = content.find_all('p')[6].text
index = fact_start.find(':') + 2
fact = fact_start[index:]

# chance commas to bars so it's not separated into multiple columns
f.write(name_field + "," + age + "," + title.replace(",", "|") + "," + family.replace(",", "|") + "," + reason.replace(",", "|") + "," + motivation.replace(",", "|") + "," + fact.replace(",", "|") + "\n")

f.close()