#! python3
# mapIt.py - inicia uma coordenada no browser usando endereços a partir da
# command line ou do clipboard (área de transferência/trabalho)

import webbrowser, sys, pyperclip #importando as bibliotecas necessarias
if len(sys.argv)>1: #se a var argv for >1 (na posicao 0 do vetor, esta mapIt)
    address = ' '.join(sys.argv[1:]) #pega o endereço da linha de comando
else:
    address = pyperclip.paste() #pega o endereço pelo clipboard - crtl+c

webbrowser.open('https://www.google.com/maps/place/' + address) #abre o local
#no google maps
