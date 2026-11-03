import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

response = requests.get(url, timeout=10) #10 seconds timeout

print("Status Code:", response.status_code)

#create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.title.text) # this will print the title of the page

books = soup.select("article.product_pod")

print("Total books:", len(books))

# for book in books:
#     print(book.h3.a["title"])


# book_data = []

# for book in books:
#     #print("Title:", book.h3.a["title"])
#     price = book.find("p", class_="price_color")
#     #print("Price:", price.get_text(strip=True))
#     avialibility = book.find("p", class_="instock availability")
#     #print("Availability:", avialibility.get_text(strip=True))
#     rating = book.find("p", class_="star-rating") #['star-rating', 'Three'] we only want second index
#     #print("Rating:", rating.get("class")[1])
#     #print("-------------------")

#     book_link = urljoin(url, book.h3.a.get("href"))  
#     detail_response = requests.get(book_link, timeout=10)
#     detail_soup = BeautifulSoup(detail_response.content, "html.parser") #HTML of an individual book
#     #print(detail_soup.prettify())
#     desc = detail_soup.find("div", id="product_description")
#     description = desc.find_next_sibling("p").get_text(strip=True)
#     #print(description)

#     book_dict = {
#         "title": book.h3.a["title"],
#         "price": price.get_text(strip=True),
#         "availability": avialibility.get_text(strip=True),
#         "rating": rating.get("class")[1],
#         "description": description
#     }
#     book_data.append(book_dict)



# print("Total records:", len(book_data))
# print(book_data[0])

#print("Total books:", len(book_data))

# for item in book_data:
#     print(item["title"], "->", len(item["description"]))


# for book in books:
#     desc = book.find("div", id="product_description")
#     print("Description:", desc.p.string)


#Testing the urljoin function to get the absolute url of the book detail page
# for book in books:
#     book_link = book.h3.a.get("href")
#     absolute_url = urljoin(url, book_link)
#     print(absolute_url)


#only first book for testing
# for book in books:
#     book_link = urljoin(url, book.h3.a.get("href"))  
#     detail_response = requests.get(book_link, timeout=10)
#     detail_soup = BeautifulSoup(detail_response.content, "html.parser") #HTML of an individual book
#     #print(detail_soup.prettify())
#     desc = detail_soup.find("div", id="product_description")
#     description = desc.find_next_sibling("p").get_text(strip=True)
#     print(description)
#     print("-------------------")




book_data = []

current_url = url

while current_url:

    try:
        response = requests.get(current_url, timeout=10)
        response.raise_for_status() # reterive the status from server and raise an exception if the status code indicates an error
        soup = BeautifulSoup(response.content, "html.parser")

    except requests.RequestException as e:
        print("Page request failed:", e)
        break

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # -------------------------   Existing code  ------------------------------------
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").get_text(strip=True)

        availability = book.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        rating = book.find("p", class_="star-rating").get("class")[1]

        # Detail page
        book_link = urljoin(current_url, book.h3.a.get("href"))

        detail_response = requests.get(book_link, timeout=10)
        detail_soup = BeautifulSoup(detail_response.content, "html.parser")

        desc = detail_soup.find("div", id="product_description")
        description = desc.find_next_sibling("p").get_text(strip=True)

        book_dict = {
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "description": description
        }

        book_data.append(book_dict)

    # Find next page
    next_page = soup.find("li", class_="next")

    if next_page:
        current_url = urljoin(current_url, next_page.a.get("href"))
    else:
        current_url = None

# print("Total records:", len(book_data))

#Travel category mein sirf 11 books hain aur next page nahi hai. Isliye ye loop ek hi baar chalega. Lekin doosri multi-page categories par automatically next pages scrape karega.


with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.DictWriter(file, fieldnames=[
        "title",
        "price",
        "availability",
        "rating",
        "description"
    ])

    writer.writeheader()
    writer.writerows(book_data)

print("Data successfully saved to books.csv")



