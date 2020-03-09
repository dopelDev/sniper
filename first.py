from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = open('index.html', 'r')
sopu = BeautifulSoup(html, 'html.parser')

#print(sub1.index())

sub1 = sopu.find_all('a', href=True, title=True)

num = 0
listOfArticles = []

for link in sub1:
    page = {}
    print(str(num) + ' : ', end='')
    print('title : ' + link['title'].replace('Enlace a', ''))
    print('link : ' + link['href'])
    page = {'numero' : num, 'title' : link['title'].replace('Enlace a', ''), 'link' : link['href']}
    listOfArticles.append(page)
    num += 1

print('\n\n\n\n')

for page in listOfArticles:
    print(page)
    print('\n\n')
