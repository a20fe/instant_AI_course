from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response =requests.get(url)
html_content =response.content
soup=BeautifulSoup(html_content ,'html.parser')

books = soup.find_all('article', class_='product_pod')


for book in books:
    book_name = book.find('h3').text.strip()
    price =book.find("p", class_="price_color").get_text().strip()
    rating = book.p["class"][1]   
    print(f"book name: {book_name}")
    print(f"book Price: {price}")
    print(f"bool Rating: {rating}")
    print("----------")
    
