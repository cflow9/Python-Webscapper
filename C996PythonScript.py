# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:06:37 2020

@author: chris
"""
import requests

from bs4 import BeautifulSoup

import csv

url = 'https://www.census.gov/programs-surveys/popest.html'

r = requests.get(url)
    

raw_html = r.content
#print(raw_html)
all_links=[]
noNone = []
links=[]
markup=[]
#parsing the    html 
soup = BeautifulSoup(raw_html, 'html.parser')
#looping through all the 'a' tags if it has a href attribute
for link in soup.find_all('a'):
    temp= link.get('href')
    #print(temp)
    if temp != None:
        noNone.append(temp)
        #print(temp)
for html in noNone:
    if  html.endswith('/') or 'html' in html:
        links.append(html)  
    else:
        slashLink = html + '/'
        links.append(slashLink)
        #print(slashLink)

for resLinks in links:
    if resLinks.startswith('#'):
        deleteHash = resLinks
    elif resLinks.startswith('http'):
        markup.append(resLinks)
    else:
        absLinks = 'https://www.census.gov' + resLinks
        markup.append(absLinks)

uniqueLinks = set(markup)
with open("C996AssignmentFinal.csv", "w") as csv_file:
  writer = csv.writer(csv_file,delimiter="\n")
  writer.writerow(uniqueLinks)
        
        
