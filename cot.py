from groq import Groq
from settings import model_start, groq_apy_key
import asyncio

class CotCadeiaDePensamentos:
    def __init__(self):
        self.__key = groq_apy_key
        self.__model = model_start
        self.client = Groq(api_key=self.__key)

    async def initial_run(self):
        """
        Docstring para initial_run
        
        :param self: Apnas fazendo o código rodar.
        """

        system_prompt = "Você é um pesquisador de carros antigos."
        context_user = "Descreva a sensação de pilotar um mustang"

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=1.5,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": context_user
                }
            ]
        )

        response = response_complete.choices[0].message.content

        print(f'Pergunta: {context_user}')
        print(f'Resposta: {response}')

        return response
    
async def run_main():
    cadeia_de_pensamentos = CotCadeiaDePensamentos()
    await cadeia_de_pensamentos.initial_run()

asyncio.run(run_main())