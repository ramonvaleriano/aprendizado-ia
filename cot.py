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
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context_user},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Pergunta: {context_user}")
        print(f"Resposta: {response}")

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
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response

    async def cot_in_health(self):
        system_prompt = """
        Você é um médico que usa Chain of Thoughts (CoT) para raciocinio clínico.
        Sempre apresente hipótese dentro do <cot> e finalize com recomendação objetiva.
        """

        user_prompt = """
        Paciente: 45 anos, sedentário, fumante, apresenta dores no peito durante esforço físico.
        Exames iniciais: colesterol alto pressão arterial elevada.

        Qual deve ser a recomendação inicial para o paciente?
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

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response
    
    async def investiment_analysis(self):
        system_prompt = """
        Voce é um consultor financeiro que usa Chain of Thoughts (CoT).
        Mostre seu raciocinio dentro de <cot> e termine com uma recomendação objetiva.
        """

        user_prompt = """
        Uma startup de tecnologia está levantando R$ 5 Milhões
        Dados:
        - Receita atual: R$ 300mil/mês
        - Crescimento: 12% ao mês
        - Equipe: 20 pessoas
        - Concorrência: forte no mercado nacional
        - Risco: dependência de um único grande cliente

        Devo recomendar o investimento?
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

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response
    
    async def product_manage(self):
        system_prompt = """
        Você é um Product Manager que usa Chain of Thoughts (CoT).
        Mostre o raciocínicio dentro de <cot> e finalize com a priorização.
        """

        user_prompt = """
        Estamos desenvolvendo um aplicativo de bem-estar:
        Funcionalidades propostas:
        1.  Meditação guiada
        2. Monitoramento e sonos
        3. Gamificação de hábitos
        4. Relatórios pesonalizados

        Orçamento permite lançar apenas duas MVP.
        Qual priorizar?
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.3,
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

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response


async def run_main():
    cadeia_de_pensamentos = CotCadeiaDePensamentos()
    await cadeia_de_pensamentos.product_manage()


asyncio.run(run_main())
