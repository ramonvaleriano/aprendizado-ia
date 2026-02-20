from groq import Groq

from settings import MODEL_START, GROQ_API

class StructuringOutput:
    def __init__(self):
        self.__model = MODEL_START
        self.__api_key = GROQ_API
        self.client = Groq(api_key=self.__api_key)



async def run_main():
    structuring_output = StructuringOutput()