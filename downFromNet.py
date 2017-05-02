import requests #importa a biblioteca que faz download de paginas
res = requests.get('http://www.gutenberg.org/files/54639/54639-0.txt')
#prepara para fazer o download do endereco desejado
try:
    res.raise_for_status() #checka se nao ouve algum erro com o endereco
except Exception as exc:
    print('There was a problem: %s' %(exc)) #caso tenha algum problema com o
#link, entao o programa é interrompido e aparece uma mesagem para alertar
#o usuario que a operacao nao pode ser concluida
dwFile = open('Naturalist\'s Repository.txt', 'wb')
#nomeia o arquivo de texto, formatando-o em .txt com conversao do binário
for chunk in res.iter_content(100000):
    dwFile.write(chunk)
#numero de bytes sendo captado a cada iteracao, colocando as strings em
#cada posicao do vetor
dwFile.close() #fecha o arquivo
