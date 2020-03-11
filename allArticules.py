from requests import get
from bs4 import BeautifulSoup
from os import mkdir
from os.path import exists
from gtts import gTTS

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


def getContent(url):

    html = get(url)
    sopa = BeautifulSoup(html.text, 'html.parser')
    listofContent = []

    chunks = sopa.find_all('p', style=True)

    for chunk in chunks:
        content = chunk.get_text()

        if 'Compartir en Facebook' in content:
            continue
        else:
            listofContent.append(content)

    return listofContent

#here begins

listOfArticles = getArticles(urlSeed)

for article in listOfArticles:
    listofContent = getContent(article['link'])
    allcontent = ''
    for content in listofContent:
        allcontent += content
    directoryName = article['title']
    if exists(directoryName):
        print(directoryName)
        continue
    else:
        mkdir(directoryName)
        tts = gTTS(allcontent, lang='es-us')
        tts.save(directoryName + '/' + directoryName + '.mp3')
        print(directoryName)
        print('sucess')
