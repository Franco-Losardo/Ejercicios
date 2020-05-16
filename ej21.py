import requests
from bs4 import BeautifulSoup
# Here you enter the site's url where you want to get the titles from
r = requests.get(
    "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
# Converts HTML into string
html = r.text
soup = BeautifulSoup(html, features="html.parser")
# Creates a file with the name given by the user which will store the article
name = input("Enter the name you want the file to have: ")
with open(name, 'w') as open_file:
    for lines in soup.find_all("p"):

      open_file.write(str(lines.getText()))
