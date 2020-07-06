# -*- coding: utf-8 -*-
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep




# _url = 'https://web.whatsapp.com/'
# driver = Chrome()
# driver.implicitly_wait(30)
# # bot = Bot()
# lista = (By.ID, 'pane-side')
# grupo_name = '6 Homens e 1/2'
# # grupo_name = 'Anotações'
# grupo = (By.XPATH, f"//span[@title='{grupo_name}']")
# Ler_mensagens = (By.XPATH, '//div[@class="z_tTQ"]')
# Ler_mensagens2 = (By.XPATH, '//div[@class="_3sKvP wQZ0F"]')
# recebido = (By.XPATH, '//div[@class="_2-dPL"]')
# box_msg = (By.CLASS_NAME ,'_3uMse')
# btn = (By.XPATH, f'//span[@data-icon="send"]')
# driver.get(_url)
# sleep(15)

# def groupo():
#     for grupos in driver.find_elements(*lista):
#         grupos.find_element(*grupo).click()
#         sleep(2)
#
# def ler_msg():
#     conv = list()
#     for total in driver.find_elements(*Ler_mensagens):
#         for texto in total.find_elements(*Ler_mensagens2):
#             if texto.find_element(*recebido).is_displayed() == True:
#                 print(texto.text)
    #         conv.append(total.text.split('\n'))
    # print(conv)
    # print(conv[0][-3], conv[0][-2])

# groupo()
# ler_msg()


# driver.close()
# driver.quit()

#
# import pymsteams
#
#
#
# myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/150f553b-b4f3-45b6-9405-d4c73c42b70a@55a2bc67-aec1-4ad2-9a9c-5b2457b91dcd/IncomingWebhook/eb3354cbe3954b7c8823f35de5d03ca9/ac621ff2-a9de-4f3d-91ec-2db034072c8e").
# # myTeamsMessage.text("api")
# # myTeamsMessage.text()
#
# print(requests.get(myTeamsMessage.last_http_response).text)