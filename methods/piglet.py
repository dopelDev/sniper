from requests import get
from bs4 import BeautifulSoup
from requests.exceptions import (HTTPError, MissingSchema, ConnectionError)
from shutil import which
from os import system


class piglet(object):
    """docstring for piglet.
        base de los scrapies"""

    def __init__(self):
        print('__init__.piglet')
        self.http = ''
        self.code = ''
        self.connectionSucess = False

    def addUrl(self, url):
        try:
            self.html = get(url)
            self.code = self.html.status_code

        except (ConnectionError, MissingSchema, HTTPError) as error:
            print(error)

    def confirmEnabled(self):
        if self.code == 200:
            self.connectionSucess = True
        else:
            self.connectionSucess = False


class winnie(piglet):
    """docstring for winnie.
        retorna una lista con
        el contenido del articulo"""

    def __init__(self, url):
        super().__init__()
        print('__init__.winnie')

        self.url = url
        super().addUrl(self.url)
        self.article = []

    def getArticle(self):
        super().confirmEnabled()
        if self.connectionSucess is True:
            soup = BeautifulSoup(self.html.text, 'html.parser')
            chunks = soup.find_all('p', style=True)

            for chunk in chunks:
                content = chunk.get_text()
                if 'Compartir en Facebook' in content:
                    continue
                else:
                    self.article.append(content)

        return self.article


class rabbit(piglet):
    """docstring for rabbit.
        scrapea las paginas
        para obtener los
        titulos y urls"""

    def __init__(self, url):
        super().__init__()
        print('__init__.rabbit')
        self.url = url
        self.pageListLinks = []
        self.beginPage = 0
        self.finalPage = 0

    def setBeginAndFinal(self, final, begin=None):
        if begin is None:
            self.finalPage = final
        else:
            self.beginPage = begin
            self.finalPage = final

    def getLinks(self):
        if self.connectionSucess is True:
            soup = BeautifulSoup(self.html.text, 'html.parser')
            page = soup.find_all('a', href=True, title=True)

            for link in page:
                article = {'title': link['title'].replace('Enlace a', ''),
                           'link': link['href']}
                self.pageListLinks.append(article)

            return self.pageListLinks

        else:
            return 'cant be connection'

    def getListLinks(self):

        if self.finalPage == 0 and self.beginPage == 0:
            super().addUrl(self.url)
            super().confirmEnabled()
            finalList = self.getLinks()

            return finalList

        elif self.finalPage != 0 and self.beginPage == 0:
            finalList = []
            for i in range(self.finalPage):
                if i == 0:
                    super().addUrl(self.url)
                    super().confirmEnabled()
                    finalList.append(self.getLinks())
                elif i > 0:
                    page = i + 1
                    url = self.url + 'page/' + str(page)
                    super().addUrl(url)
                    super().confirmEnabled()
                    finalList.append(self.getLinks())

            return finalList

        elif self.finalPage != 0 and self.beginPage != 0:
            finalList = []
            for i in range(self.beginPage, self.finalPage + 1):
                page = i
                url = self.url + 'page/' + str(page)
                super().addUrl(url)
                super().confirmEnabled()
                finalList.append(self.getLinks())

            return finalList


def makeMkv(mp3, jpeg):
    """Short summary.

    Parameters
    ----------
    mp3 : type mp3
        Description of parameter:
        el sonido de fondo.
    jpeg : type jpeg
        Description of parameter:
        la imagen de fondo.

    Returns
    -------
    type
        Description of returned:
        un video en formato mkv.

    """
    while True:
        if which('ffmpeg') is not None:
            title = mp3.replace('.mp3', '')
            string = "ffmpeg -loop 1 -framerate 1 -i '{}' -i ".format(jpeg)
            string = string + "'{}' -c copy -shortest '{}.mkv'".format(mp3,
                                                                       title)
            system(string)
            break
        else:
            system('sudo apt install ffmpeg')
