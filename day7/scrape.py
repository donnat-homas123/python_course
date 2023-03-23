import requests
from bs4 import BeautifulSoup

req=requests.get('https://www.cet.ac.in/head-of-departments/')
source_code=req.content
soup= BeautifulSoup(source_code,'lxml') #print(soup)

figure_element=soup.find('figure',class_='wp-block-table') 
print(figure_element)

table=figure_element.find('table')  
print(table)

table_rows=table.find_all('tr')     
print(table_rows)   #,also output in a list

table_rows=table_rows[1:]  
#print from name,dept and phone of people only so avoid first row

for row in table_rows:
    tds=row.find_all('td')
    name=tds[0].text
    print(name)
    dept=tds[1].text
    print(dept)
    phn=tds[2].text
    print(phn)


"""
for row in table_rows:
    tds=row.find_all('td')
    name=tds[0].text
    print(name)

for row in table_rows:
    tds=row.find_all('td')
    dept=tds[1].text
    print(dept)
for row in table_rows:
    tds=row.find_all('td')    
    phn=tds[2].text
    print(phn) 
    """
