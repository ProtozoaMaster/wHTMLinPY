#! python3
# lucky.py - abre varias abas de uma pesquisa no google

import requests, sys, webbrowser, bs4

print('Googling...') #texto apresentado junto com o download da página do Google
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) #a var.
#pega as strings do site e armazena no vetor
res.raise_for_status() #confirma se o download da pagina esta sendo feito de maneira correta

soup = bs4.BeautifulSoup(res.text, 'html.parser') #capta os primeiros resultados disponiveis
linkElems = soup.select('.r a') #abre uma nova aba para cada resultado

#a funcao abaixo ira abrir, cinco ou o tamanho da variavel de abas no web browser
#atraves da iteracao que sera realizada a qtdade de vezes do tamanho de numOpen
#que tamber ira conter 5 ou o tamanho minimo do resultado da pesquisa (as vezes
#a pequisa ira retornar menos que 5 resultados, entao sera do tamanho minimo de
#resultados que ela retornar). A ultima linha do codigo apenas abre as paginas
#no browser em novas abas.
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

#as referencias .r, a, href sao devidos ao jeito de programacao HTML
#onde, usualmente, r e referido para resultado de pesquisas, a para abertura
#de codigos de links, e href o DNS do site
