#!/usr/bin/python3

# temporal imports
from sys import executable
from requests import get, codes
print(executable)
# para generar las paginas

def gen_pages(URL : str, word : str) ->  list:
    # instancen VARs
    result : list = []
    count : int  = 0
    page : int = 1
    while True:
        tmp = URL + word + str(page)
        print('comprovando : \t {}'.format(tmp))
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


print(gen_pages(URL = 'http://www.elfrancotirador.com', word = '/page/'))
