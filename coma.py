from json import dump as jsDump
from sys import path
from os import listdir, getcwd
path.append('/home/dopel/projects/myPlayground/sniper/methods')
from piglet import rabbit


def main():
    conejo = rabbit('http://www.elfrancotirador.com/')
    conejo.setBeginAndFinal(13)
    listaDeArticulosYUrls = conejo.getListLinks()
    listOfFile = listdir(getcwd())
    if 'articulos.json' in listOfFile:
        print('ya existe el archivo json')
        file = open('articulos.json', 'w')
        jsDump(listaDeArticulosYUrls, file, sort_keys=True, indent=(4))
        file.close()
    else:
        print('no existe y se creara un archivo')
        file = open('articulos.json', 'w+')
        jsDump(listaDeArticulosYUrls, file, sort_keys=True, indent=(4))
        file.close()


if __name__ == '__main__':
    main()
