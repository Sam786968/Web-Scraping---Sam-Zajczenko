# make sure you fork this and git repo it
# go to the shell command screen and type
# pip install -r requirements.txt
#to install the necessary components
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Best-Sellers-Books/zgbs/books"
headers = {
  'user-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#get all books
# print(books[0].prettify())
# focus on rankings to make ordering easier
# book = books[0]
# rank = book.find('span', class_='zg-bdg-text').text[1:]
# print(rank)
# children = book.find('div', class_='zg-grid-general-faceout').div
# title = children.contents[1].text
# author = children.contents[2].text
# rating = children.contents[3].text
# price = children.contents[-1].text
# print(title,author,rating+", ratings")

import csv
import pandas as pd

books = soup.find_all(id="gridItemRoot")

csv_headers = ['Rank', 'Title', 'Author', 'Price']

with open('amazon_books.csv', 'w', encoding = 'utf-8', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(csv_headers)

for item in books:
  children = item.find('div', class_='zg-grid-general-faceout').div

  rank = item.find('span', class_='zg-bdg-text').text[1:]
  title = children.contents[1].text
  author = children.contents[2].text
  # rating = children.contents[3].text
  price = children.contents[-1].text

  with open('amazon_books.csv', 'a', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([rank, title, author, price]) 