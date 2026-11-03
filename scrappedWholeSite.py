import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
print(soup.select_one("ol.row").prettify())