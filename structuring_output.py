from groq import Groq

from settings import groq_apy_key, model_start

class StructuringOutput:

    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=groq_apy_key)

    