import requests
from bs4 import BeautifulSoup

#Link da pagina
quotes_url = "https://twitch.center/customapi/quote/list?token=25693f14"

#Request da pagina
pagina = requests.get(quotes_url)
#Conteúdo da pagina em uma grande string
texto = pagina.text

#Cria uma lista com todas as frases separadas pelo delimitador de linha \n
frases = texto.splitlines()
#print(frases)
print(len(frases), "quotes.")