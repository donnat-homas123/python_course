file_to_write=open("books_scrape.txt","w", encoding="utf-16")

import requests
from bs4 import BeautifulSoup

req=requests.get('https://books.toscrape.com/')
#for loop for going to next pg
source_code=req.content
soup= BeautifulSoup(source_code,'lxml') 

articles=soup.find_all('article',class_='product_pod') 
print(articles)

for article in articles:
    #print(article.find('h3'))
    h3_tag=article.find('h3')
    #print(h3_tag.find('a'))
    a_tag=h3_tag.find('a')
    #print(a_tag['title'])
    name=a_tag['title']

    #to find price

    div =article.find('div',class_='product_price')
    #print(div)
    p_tag=div.find('p')
    #print(p_tag)
    price=p_tag.text
    #print (p_tag.text)

    line_to_write=name+'  '+price+'\n'
    file_to_write.write(line_to_write)
    
    
file_to_write.close()
