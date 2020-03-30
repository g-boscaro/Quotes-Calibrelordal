import bs4 as bs
import requests

quotes_url = "https://twitch.center/customapi/quote/list?token=25693f14"

pagina = requests.get(quotes_url)
print(pagina.text[0:500])