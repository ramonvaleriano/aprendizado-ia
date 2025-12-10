import asyncio
from groq import Groq

from settings import groq_apy_key, model_start


class UsingMultipleSteps:
    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=self.__api_key)

    async def multiple_steps_basic(self):
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
    
    async def multiples_steps_advanced(self):
        # Usando multiplos passos avançados
        system_prompt = """
        Você é um analista ambiental. Metodologia:
        1) Estruture os dados em tabela mental e calcule médias/medianas por bairro
        2) Detecte tendências (alta/baixa) e outliers
        3) Calcule correlações qualitativas (tráfego x PM2.5; área verde x PM2.5)
        4) Classifique risco por bairro (baixo/médio/alto) com justificativa
        5) Recomende 3 ações operacionais e 2 ações estruturais
        6) Valide limitações dos dados
        Responda com seções numeradas.
        """

        user_prompt = """
        DADOS (4 semanas, valores médios semanais):
        Bairro A: PM2.5[23, 26, 29, 31] μg/m³; Tráfego[alto]; Área verde[baixa]
        Bairro B: PM2.5[14, 13, 16, 15]; Tráfego[médio]; Área verde[média]
        Bairro C: PM2.5[11, 12, 10, 12]; Tráfego[baixo]; Área verde[alta]
        Bairro D: PM2.5[28, 35, 33, 37]; Tráfego[muito alto]; Área verde[baixa]
        Limite guia OMS (anual): 5 μg/m³ (referência).
        Aplique a metodologia.
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.3,
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
    await using_multiple_steps.multiples_steps_advanced()


asyncio.run(test_steps())
