#! python3
#allMyLinks.py - Programa para deixar abas clean e nao precisar de salvar
#favoritos e fazer backup sempre que precisar formatar ou adicionar um novo fav
#e para fazer login automaticamente na telecom

import webbrowser
from selenium import webdriver

gmail = 'http://www.gmail.com'
ufu = 'http://www.mail.ufu.br'
sisbi = 'http://babao.dr.ufu.br:8080'
diase = 'http://www.proae.ufu.br/assistencia'
#variaveis para armazenar os sites

browser = webdriver.Chrome()#abre o chrome
browser.get(gmail)#entra no gmail
emailElem = browser.find_element_by_id('Email')#procura um elemento id = 'email'
emailElem.send_keys('feeltelecom2016@gmail.com')#insere o email na chave
passwordElem = browser.find_element_by_id('Password')#procura a box da senha
passwordElem.send_keys('feelttele2017')#insere a senha
passwordElem.submit()#faz o login
#processo para abrir o Gmail e fazer o login no email da telecom

webbrowser.open(ufu)
webbrowser.open(sisbi)
webbrowser.open(diase)
#func para abrir os sites
