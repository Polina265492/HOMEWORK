import requests
from bs4 import BeautifulSoup
import lxml

url = "https://cash-backer.club/shops"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent": user}

session = requests.Session()

responce = session.get(url, headers =headers)
print(responce.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(responce.text, features:"lxml")
    elements =soup.find(name: "li", class_="class="col-lg-2 col-md-3 shop-list-card pseudo-link no-link"")
    elements = soup.find(name: "li", class_ = "class="card-body")
    elements = soup.find(name: "li", class_ = "class="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
    
    print(elements.text)


#Я не совсем понимаю как что надо делать, программа падает, сделала все что смогла(
