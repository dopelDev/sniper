#!/usr/bin/python3

# temporal imports
from sys import executable
# imports
from typing import Dict, List
from requests import get, codes
from bs4 import BeautifulSoup
from alive_progress import alive_bar

print(executable)
# para generar las paginas

def gen_pages(URL : str, word : str) ->  List[str]:
    # instancen VARs
    result = [] 
    count : int  = 0
    page : int = 1
    while True:
        tmp = URL + word + str(page)
        print('comprobando : \t {}'.format(tmp))
        response = get(tmp)
        if response.status_code == codes.ok:
            print('{} \t found'.format(tmp))
            result.append(tmp)
            count = 0
        else:
            print("{} \t don't found".format(tmp))
            count+=1
        # si no cuentra 2 seguidas break
        if count > 1:
            break
        page+=1
    return result


# print(gen_pages(URL = 'http://www.elfrancotirador.com', word = '/page/'))

# obtener las url de los cada pagina

def get_urls(URL : str) -> List[Dict[str, str]] :
    results = []
    response = get(URL)
    # hacer la sopa
    if response.status_code == codes.ok:
       sopa = BeautifulSoup(response.text, 'html.parser')
    datos = sopa.find_all('a', href=True, title=True)
    for data in datos:
        article = {'title' : data['title'], 'link' : data['href']}
        results.append(article)
    return results

def get_articules(title : str, Url : str):
    pass

# recibe una list conteniendo los titulos y url de cada pagina
def clean_titles(articles : List[Dict[str,str]]):
    for article in articles:
        tmp = article.get('title')
        tmp = tmp.replace('Enlace a ', '')
        article.update([('title', tmp)])


