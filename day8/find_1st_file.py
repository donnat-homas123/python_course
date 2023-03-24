file_to_write=open("book_scrape.txt","w")

import requests
from bs4 import BeautifulSoup

req=requests.get('https://books.toscrape.com/')
source_code=req.content
soup= BeautifulSoup(source_code,'lxml') 

figure_element=soup.find('article',class_='product_pod') 
table=figure_element.find('h3')
a = table.find('a')
print(a)
print(a['title'])
line_to_write=a['title']
file_to_write.write(line_to_write)
    
    
file_to_write.close()