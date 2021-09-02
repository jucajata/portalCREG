
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

#Obtendremos la resolución y la transformaremos según el año
print('-----------------------------------------------------------')
resolucion = input('Escriba la resolución CREG (pj: CREG###-yyyy): CREG')
CREG = 'CREG'
number = resolucion[:3]
#print(resolucion)
#print(number)
year = resolucion[-4:] #Obtengo el año
resolucion = CREG + number + '-' + year
if year == "1999":
    y = "99"
    resolucion = CREG + number + '-' + y
elif year == "1998":
    y = "98"
    resolucion = CREG + number + '-' + y
elif year == "1997":
    y = "97"
    resolucion = CREG + ' ' + number + '/' + y
elif year == "1996":
    y = "96"
    resolucion = CREG + ' ' + number + '/' + y
elif year == "1995":
    y = "95"
    resolucion = CREG + ' ' + number + '/' + y
elif year == "1994":
    y = "94"
    resolucion = CREG + ' ' + number + '/' + y

#print(resolucion)
url = 'http://apolo.creg.gov.co/Publicac.nsf/Documentos-Resoluciones?openview=%27'
urlprin = 'http://apolo.creg.gov.co'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('img')
#print(tags)
x = None
url_new2 = None

#Buscamos el año que ingresaron en el input
i = -1
for tag in tags:
    detail = tag.get('alt', None)
    detail = detail.split()
    try:
        year_creg = detail[-1]
        #print(year_creg)
        i += 1
        if int(year) == int(year_creg):
            #print("Encontrado en:",year)
            #print(i)
            break
    except:
        continue

#Buscamos el link para hacer la búsqueda
x = None
url_new2 = None
tags = soup('a')
tag = tags[i]
url2 = tag.get('href', None)
url3 = url2.replace('Count=30','Count=1000')
url_new = urlprin + url3
html = urllib.request.urlopen(url_new, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags_new = soup('a')
for tag_new in tags_new:
    #print(tag_new.get_text())
    if tag_new.get_text() == resolucion:
        url_new2 = str(urlprin + tag_new.get('href', None))
        #print('Encontrada resolución en: ', url_new2)
        x = True
        if x == True:
            break
    else:
        continue

from selenium import webdriver
import time

driver = webdriver.Chrome()
link = url_new2
driver.get(link)
