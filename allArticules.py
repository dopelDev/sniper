from requests import get
from bs4 import BeautifulSoup
from pprint import pprint
urlSeed = 'http://www.elfrancotirador.com/'

def getArticles(urlSeed):

    listOfArticles = []

    numPage = 1

    while (True):

        article = {}

        if numPage is 1:

            print(urlSeed)
            print('\n\n')
            html = get(urlSeed)
            code = html.status_code
        else:

            print(urlSeed + 'page/' + str(numPage))
            print('\n\n')
            html = get(urlSeed + 'page/' + str(numPage))
            code = html.status_code

        if code == 200:

            sopa = BeautifulSoup(html.text, 'html.parser')
            page = sopa.find_all('a', href=True, title=True)

            for link in page:
                article = {'title' : link['title'].replace('Enlace a', ''), 'link' : link['href']}
                listOfArticles.append(article)

        elif code == 404:

            return listOfArticles
            break

        numPage += 1


#here begins

list = getArticles(urlSeed)

pprint(list)
