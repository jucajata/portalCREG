# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

resolucion = input('Escriba la resolución CREG (pj: CREG107-2008): ')

#url = input('Enter - ')
url = 'http://apolo.creg.gov.co/Publicac.nsf...
urlprin = 'http://apolo.creg.gov.co'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
ppaltags = []
x = None
url_new2 = None
for tag in tags:
    ppaltags.append(tag.get('href', None))
    url2 = tag.get('href', None)
    url3 = url2.replace('Count=30','Count=1000')
    url_new = urlprin + url3
    html = urllib.request.urlopen(url_new, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags_new = soup('a')
    for tag_new in tags_new:
        print(tag_new.get_text())
        if tag_new.get_text() == resolucion:
            url_new2 = str(urlprin + tag_new.get('href', None))
            print('Encontrada resolución en: ', url_new2)
            x = True
            break
        else:
            continue
    if x == True:
        break

from selenium import webdriver
import time

driver = webdriver.Chrome()
link = url_new2
driver.get(link)
time.sleep(100)
driver.close()
