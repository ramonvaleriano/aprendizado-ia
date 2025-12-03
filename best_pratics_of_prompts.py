from groq import Groq

from settings import groq_apy_key, model_start

class BestPraticsOfPrompts:
    """
        Use Prompts especificos
        Instruções Precisas e Detalhadas
        Controle o formato da resposta
        Use separadores para organizar informações
    """
    def __init__(self):
        self.__api_key = groq_apy_key
        self.__model = model_start
        self.client = Groq(api_key=self.__api_key)

    def first_prompt(self):
        pass