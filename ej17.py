import requests
from bs4 import BeautifulSoup
# Here you enter the site's url from where you want to get the titles
r = requests.get('https://lanacion.com.ar')
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
h1_titles = soup("h1")
h2_titles = soup("h2")
print(h1_titles, h2_titles)
