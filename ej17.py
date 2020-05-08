import requests
from bs4 import BeautifulSoup
# Here you enter the site's url from where you want to get the titles
r = requests.get('https://lanacion.com.ar')
# Converts HTML into string
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
# Here you enter the HTML tag that containes the titles you want to print
# Gives format to the output, the loop removes the spaces and gets rid
# of all the HTML stuff

for titles in soup(class_="com-title"):
    if titles.a:
        print(titles.a.text.replace("\n", "").strip())
    else:
        print(titles.contents[0])
