# -*- coding: utf-8 -*-
from requests import get
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from Modelos import Bot


class Whats:

    def __init__(self):

        self._url = 'https://web.whatsapp.com/'
        self.driver = Chrome()
        self.driver.implicitly_wait(30)
        self.bot = Bot()
        self.lista = (By.ID, 'pane-side')
        self.grupo_name = input('Insira o nome de um contato ou grupo: ')
        self.grupo = (By.XPATH, f"//span[@title='{self.grupo_name}']")
        self.Ler_mensagens = (By.XPATH, '//div[contains(@class,"message-in focusable-list-item")]')
        self.box_msg = (By.CLASS_NAME,'_3uMse')
        self.btn = (By.XPATH, f'//span[@data-icon="send"]')
        self.driver.get(self._url)
        sleep(10)

    def groupo(self):
        print('Procurando grupo...')
        for grupos in self.driver.find_elements(*self.lista):
            grupos.find_element(*self.grupo).click()
            sleep(2)

    def ler_msg(self):
        conv = list()
        for total in self.driver.find_elements(*self.Ler_mensagens):
            conv.append(total.text.split('\n')[-2])
        return conv[-1]

    def envia_msg(self, msg = None):
        if msg != None or msg != '':
            Box = self.driver.find_element(*self.box_msg)
            Box.click()
            Box.send_keys(msg+'\n')
            print(msg)
        else:
            pass

    def conversas(self):
        self.bot.aprender()
        conversas = set()
        self.groupo()
        self.envia_msg('Assistente iniciado!!')
        conversas.add('Assistente iniciado!!')
        print('Procurando Mensagens!!')
        while True:
            al = self.ler_msg()
            if al not in conversas:
                print(al)
                bot = self.bot.retorno_chat(al)
                conversas.add(al)
                conversas.add(str(bot))
                self.envia_msg(str(bot))


Bot_Whats = Whats()
Bot_Whats.conversas()
