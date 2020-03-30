#Teste de funcionamento de Expressões regulares

#importa a biblioteca de regex
import re

#String de teste
quote = r'15. "Meu Deus, eu encostei numa menina, mano" -Saga'

#A expressão captura um grupo(), define um caracter no range de 0 a 9 [0-9], e faz o match de um a infinitos caracteres +
#.group() define qual o grupo achado será utilizado
num_quote = re.search(r'([0-9]+)', quote).group()
#print(num_quote)
print("Numero do quote:", num_quote)

txt_quote = re.search(r'"([^\"]*)"', quote).group(1)
#print(texto_quote)
print("Quote:", texto_quote)

#autor_quote = re.search(r'([^-]\w+$)', quote)
autor_quote = re.search(r'([^-]\w+$)', quote).group()
#print(autor_quote)
print("Autor:", autor_quote)



#lista_quotes = ["""1. "Coma pizza todo dia" - Saga""", """2. "Charge characters are for low IQ idiots" -LTG"""]

#for quote in lista_quotes:
    #find_quote = re.search('"([^\"]*)"', quote)
    #find_autor = re.findall()
    #print(find_quote)
