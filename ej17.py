import requests
from bs4 import BeautifulSoup
# Here you enter the site's url from where you want to get the titles
r = requests.get('https://lanacion.com.ar')
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
# Here you enter the HTML tag that containes all those titles you want to print
h1_titles = soup(class_="com-title")
print(h1_titles)
