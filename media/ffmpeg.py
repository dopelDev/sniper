from os import system
import sys
sys.path.append('/home/dopel/projects/myPlayground/sniper/methods')
from piglet import rabbit as conejo, winnie as oso
from gtts import gTTS


def makeMkv(mp3):
    mp3 = ' El músico, el torero y el poeta.mp3'
    string = "ffmpeg -loop 1 -framerate 1 -i download.jpeg -i "
    string = string + "'{}' -c copy -shortest '{}.mkv'".format(mp3, mp3)
    system(string)


conejo = conejo('http://www.elfrancotirador.com/page/12/')
lista = conejo.getListLinks()

for i in range(len(lista)):

    print(lista[i]['title'][1:])
    print(lista[i]['link'])
