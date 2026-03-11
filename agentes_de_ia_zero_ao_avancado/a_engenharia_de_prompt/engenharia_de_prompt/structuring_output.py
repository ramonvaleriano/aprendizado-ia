from groq import Groq

from settings import MODEL_START, GROQ_API

class StructuringOutput:
    def __init__(self):
        self.__model = MODEL_START
        self.__api_key = GROQ_API
        self.client = Groq(api_key=self.__api_key)
        self.system_prompt = None
        self.user_prompt = None

    async def first_structuring_output(self):
        pass


async def run_main():
    structuring_output = StructuringOutput()