import wikipedia
from google import google
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot_corpus.data import portuguese


class Bot:

    def __init__(self):
        self.bot = ChatBot('Chat')

    def aprender(self):
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train('chatterbot.corpus.portuguese')

    def retorno_chat(self, query):
        resposta = self.bot.get_response(query)
        if float(resposta.confidence) > 0.5:
            return resposta
        elif query.startswith('quanto é '):
            resposta = eval(query.replace('quanto é ',''))
            return resposta
        else:
            resposta = self.consulta(query)
            return resposta




    def normalizar_str(self, text):
        pchave = ['quem foi', 'quem é', 'quando ocorreu', 'quando aconteceu']
        text = text.strip().lower()

        for part in pchave:
            if text.startswith(part.lower()):
                return text.replace(part, "").strip()

        return text

    def consulta_google(self, query):
        for search_results in google.search(query, 2):
            result = search_results.description
            if search_results.google_link:
                link = search_results.google_link
            elif search_results.link:
                link = search_results.link
            else:
                pass

            return result +'\n'+ str(link)

    def consulta(self, query):
        query = self.normalizar_str(query)

        try:
            wikipedia.set_lang('pt')
            return wikipedia.summary(query, sentences=1)
        except:
            return self.consulta_google(query)

Bot()