from groq import Groq
from settings import model_start, groq_apy_key
import asyncio

class CotCadeiaDePensamentos:
    """
    Raciocinio estrutura e explícito
    Explicação transparente do Raciocinio
    Clareza na tomada de decisão
    """
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
    
    async def marketing_strategist(self):
        system_prompt = """
        Você é um estrategista de marketing que sempre usa Chain of Thoughts (Cot).
        Mostre o raciocínio dentro de <cot> e depois dê uma conclusão objetiva.
        """

        user_prompt = """
        Uma empresa de moda quer lançar uma camapnha para atrair a Geração Z.
        Dados:
        - Orçamento: R$ 500 mil
        - Principais canais: Instragram, TikTok, YouTube
        - Objetivo: aumentar vendas online em 30% em 6 meses
        - Concorrência: 3 marcas fortes no mesmo segmento

        Crie um plano de campanha explicando o raciocínio passo a passo.
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.4,
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

        print(f'Pergunta: {user_prompt}')
        print(f'Resposta: {response}')

        return response



async def run_main():
    cadeia_de_pensamentos = CotCadeiaDePensamentos()
    await cadeia_de_pensamentos.marketing_strategist()

asyncio.run(run_main())