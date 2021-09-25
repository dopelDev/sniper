#!/usr/bin/python3.9
# imports base

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import (HTTPError, MissingSchema, ConnectionError)

# tmp imports
from sys import executable

print(executable)

# CONST
URL = 'http://www.elfrancotirador.com/'
