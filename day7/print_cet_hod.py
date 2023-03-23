file_to_write=open("cet_hod_new.txt","w")

import requests
from bs4 import BeautifulSoup

req=requests.get('https://www.cet.ac.in/head-of-departments/')
source_code=req.content
soup= BeautifulSoup(source_code,'lxml') 

figure_element=soup.find('figure',class_='wp-block-table') 

table=figure_element.find('table')  

table_rows=table.find_all('tr')        

table_rows=table_rows[1:]  

for row in table_rows:
    tds=row.find_all('td')
    name=tds[0].text  
    dept=tds[1].text
    phn=tds[2].text
    line_to_write=name+'  '+dept+'  '+phn+'  '+'\n'
    file_to_write.write(line_to_write)
    
    
file_to_write.close()