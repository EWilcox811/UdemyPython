import os
import requests
import bs4

###     Grabbing a page title   ###
result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
type(result)
result.text
soup = bs4.BeautifulSoup(result.text, "lxml")
soup.select('title')[0].getText()
soup.select('p')
soup.select('h1')[0].getText()


###     Grabbing a class    ###
text = []
table_of_contents = soup.select(".toctext")
for item in table_of_contents:
    text.append(item.getText()) # Each soup item is turned into the text that we want and appended to the text list
for item in text:
    print(item) # print out the table of contents that we scraped from the webpage


###     Grabbing an Image   ###
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup2 = bs4.BeautifulSoup(res.text, 'lxml')
image = soup2.select('.thumbimage')
computer = image[0]
computer['src']
image_link = requests.get("https:" + computer['src'])
image_link.content
f=open('my_comp_image.jpg',mode='wb' )
f.write(image_link.content)
f.close()
