#!/home/dopel/projects/myPlayground/sniper/env/bin/python3.8
from methods.piglet import rabbit as conejo, winnie as oso
from gtts import gTTS

conejo = conejo('http://www.elfrancotirador.com/')
lista = conejo.getListLinks()
lastArticle = lista[0]

print(lastArticle['title'])
print(lastArticle['link'])

oso = oso(lastArticle['link'])
texto = oso.getArticle()
voice = ''
for i in range(len(texto)):
    if texto[i] != '':
        voice = voice + texto[i]
tts = gTTS(voice, lang='es')
tts.save(lastArticle['title'] + '.mp3')

# print(texto)
