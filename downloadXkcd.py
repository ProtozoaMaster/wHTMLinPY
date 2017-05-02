#! python3
# downloadXckd.py - downloading all the comics from an website

import requests, os, bs4

url = 'http://xkcd.com' #url inicial
os.makedirs('xkcd', exist_ok=True) #armazena quadrinhos no ./xkcd e deixa claro
#que exista uma pasta pronta
while not url.endswith('#'):#enquanto o url nao termina com a str '#'
    print('Downloading page %s...' %url)#realiza o download
    res = requests.get(url)
    res.raise_for_status()#garante que nao há erro no url
    soup = bs4.BeautifulSoup(res.text, "html.parser")#a funcao fica analizando e
#buscando partes do codigo html que correspondam a variavel

    comicElem = soup.select('#comic img')#procura o url da imagem
    if comicElem == []:
        print('Could not find comic image.')#caso nao ache, printa isso
    else:
        comicUrl = comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
#caso ele ache, o programa vai armazenando dentro do vetor as imagens dentro
#do diretorio selecionado, sempre ao final da iteracao checando se o url
#esta correto para evitar erros com a func raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
#faz o processo de conversao de bits (existe 100000 bytes possiveis para serem
#preenchidos a cada iteração e convertidos e escrevidos em pedaços

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
#funcao para pegar o link anterior do quadrinho atual, para poder comecar
#toda a iteracao novamente.

print('Done.')
