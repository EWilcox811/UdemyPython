import os
import requests
import bs4

# ###     Grabbing a page title   ###
# result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
# type(result)
# result.text
# soup = bs4.BeautifulSoup(result.text, "lxml")
# soup.select('title')[0].getText()
# soup.select('p')
# soup.select('h1')[0].getText()
#
# ###     Grabbing a class    ###
# text = []
# table_of_contents = soup.select(".toctext")
# for item in table_of_contents:
#     text.append(item.getText()) # Each soup item is turned into the text that we want and appended to the text list
# for item in text:
#     print(item) # print out the table of contents that we scraped from the webpage
#
#
# ###     Grabbing an Image   ###
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup2 = bs4.BeautifulSoup(res.text, 'lxml')
# image = soup2.select('.thumbimage')
# computer = image[0]
# computer['src']
# image_link = requests.get("https:" + computer['src'])
# image_link.content
# f=open('my_comp_image.jpg',mode='wb' )
# f.write(image_link.content)
# f.close()
#
#
# ###     Books.toscrape.com  ###
# # def get_title()
# base_url = "http://books.toscrape.com/catalogue/page-{}.html"
# req = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(req.text,'lxml')
# products = soup.select(".product_pod")
# len(soup.select(".product_pod"))
# example = products[0]
# example.select(".star-rating.Three")
#
# two_star_titles = []
# for n in range(1,51):
#     scrape_url = base_url.format(n)
#     book_req = requests.get(scrape_url)
#
#     soup = bs4.BeautifulSoup(book_req.text,'lxml')
#     books = soup.select(".product_pod")
#
#     for book in books:
#         if len(book.select('.star-rating.Two')) != 0:
#             two_star_titles.append(book.select('a')[1]['title'])
# for title in two_star_titles:
#     print(title)
#
#

###     Webscraping Excercise   ###
base_url = "https://quotes.toscrape.com/page/{}/"
req = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(req.text, 'lxml')
authors = set()
for author in soup.select(".author"):
    authors.add(author.text)
authors
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print("\n\n\nQUOTES ADDED\n\n\n")


tags = soup.select(".tag-item")
type(tags[0])
len(tags)
type(tags)
tags[0].select('a')[0].text
top_ten = []
for n in range(0,10):
    top_ten.append(tags[n].select('a')[0].text)
top_ten
print("\n\n\n top ten scraped \n\n\n")
n = 1
run = True

# url2 = base_url.format(11)
# req2 = requests.get(url2)
# soup2 = bs4.BeautifulSoup(req2.txt,"lxml")
while run:
    scrape_url = base_url.format(n)
    quote_req = requests.get(scrape_url)
    if "No quotes found!" in quote_req.text:
        break
    quote_soup = bs4.BeautifulSoup(quote_req.text, "lxml")

    n+=1
for name in authors:
    print(name)
