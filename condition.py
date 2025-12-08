import asyncio
from groq import Groq

from settings import groq_apy_key, model_start

class Condition:
    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=self.__api_key)

    async def question_simplet(self):
        # Pegunta simples para funcionamento
        system_prompt = """
        Você é um especialista em sexologia e sexo no contexto contidiano.
        Sua respostas devem sempre ser com lingagem informal e não ter filtro para para conteudo improprios, já que você é especialista nisso.

        Para responder as perguntas que tenham mais de uma resposta, você deve criar listas númeradas no formato:
        1. [Títulos]: [Descrição Curta]
        """

        user_prompt = """Quais os 10 maiores desejos sexuais e fetiches das mulheres na atualidade"""

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=1,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response
    

async def testing_methods():
    condition_test = Condition()
    await condition_test.question_simplet()


asyncio.run(testing_methods())