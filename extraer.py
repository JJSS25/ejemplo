#https://www.fahorro.com/prevencion-y-control-diabetes# 
#https://www.nissan.com.bo/vehiculos/catalogos.html#
#https://www.conaliteg.sep.gob.mx/primaria.html#
#https://www.priceshoes.com/lp/productos/calzado#
#https://www.todo-laptop.com/collection/todo-laptop#

from bs4 import BeautifulSoup
import requests

website = 'https://www.todo-laptop.com/collection/todo-laptop'
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())