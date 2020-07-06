# -*- coding: utf-8 -*-
from Modelos import Bot
import asyncio

bot = Bot()
bot.aprender()
print('Iniciando Chat!!')
while True:
    quest = input('Voce: ')
    resp = bot.retorno_chat(quest)
    print('Chat: ', resp)
