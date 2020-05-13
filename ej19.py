import requests
from bs4 import BeautifulSoup
# Here you enter the site's url from where you want to get the titles
r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
# Converts HTML into string
html = r.text
soup = BeautifulSoup(html, features="html.parser")
# Prints the tag's content
for lines in soup.find_all("p"):

    print(str(lines.getText()))