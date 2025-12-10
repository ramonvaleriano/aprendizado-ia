import asyncio
from groq import Groq

from settings import groq_apy_key, model_start


class UsingMultipleSteps:
    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=self.__api_key)

    async def multiple_step_basic(self):
        # Usando multiplos passos básicos.
        system_prompt = """
        Você um guia de trekking ultraleve. Siga a metodologia multi-step
        1) Liste e some os pesos por categoria
        2) Calcule o peso-base (sem comida/água/combustível)
        3) Defina a meta de redução (15% do peso-base)
        4) Proponha trocas/reduções para alcançar a meta
        5) Verifique consitência e riscos (clima/segurança)
        Formate cada passo com títulos claros.
        """

        user_prompt = """
        PLANEJAMENTO (2 dias, clima ameno, sem chuva prevista)
        ITENS E PESOS (g):
        • Abrigo (barraca): 1450
        • Saco de dormir: 900
        • Isolante: 420
        • Mochila: 1100
        • Fogareiro: 85
        • Panela titânio: 120
        • Garrafa 1L (vazia): 110
        • Kit primeiros socorros: 160
        • Capa de chuva: 180
        • Fleece: 320
        • Camiseta extra: 110
        • Meias extra: 60
        • Lanterna: 90
        • Power bank: 210
        • Kit higiene: 140

        META: reduzir o peso-base em 15% mantendo segurança e conforto térmico.
        PASSOS: execute 1→5 conforme metodologia.
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.25,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response


async def test_steps():
    using_multiple_steps = UsingMultipleSteps()
    await using_multiple_steps.multiple_step_basic()


asyncio.run(test_steps())
