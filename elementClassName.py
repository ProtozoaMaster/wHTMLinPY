from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_elemet_by_class_name('bookcover')
    print('Found <%s> element with that class name!' %(element.tag_name))
except:
    print('Was not able to find an element with that name.')

#simples programa apenas para procurar no url um elemento especifico
#dentro do codigo html, e caso ele ache, ele printa na tela.
