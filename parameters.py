from groq import Groq
from settings import groq_apy_key, model_start

class Parameters:
    """
        temperature: Controla a alatoridade das respostas. Valores entre 0.0 e 1.0 são aceitos.
        max_completion_tokens: define o número máximo de tokens que podem ser gerados pelo modelo.
                               Esse parâmetro substitui o max_tokens em desuso.
        top_p: Controla a diversidade via "nucleus sampling" -- em torno de 0.5 significa considerar
               apenas tokens que somam 50% da probabilidade. 
    """
    def __init__(self):
        self.__api_key = groq_apy_key
        self.__model = model_start
        self.client = Groq(api_key=self.__api_key)

    def firt_chat_parameters(self):
        pass